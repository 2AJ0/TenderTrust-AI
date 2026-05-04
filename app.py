import streamlit as st
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from pypdf import PdfReader
import io

# --- 1. Setup & Configuration ---
st.set_page_config(page_title="TenderTrust AI", layout="wide")
st.title("🛡️ TenderTrust AI: CRPF Eligibility Engine")

# Note: In a real submission, use st.secrets or a .env file
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# --- 2. Logic: Extraction & Evaluation ---
def analyze_compliance(tender_text, bidder_text):
    llm = ChatOpenAI(api_key=api_key, model="gpt-4o")
    
    prompt = ChatPromptTemplate.from_template("""
    You are a Procurement Auditor for CRPF. 
    
    TENDER CRITERIA:
    {tender_text}
    
    BIDDER SUBMISSION:
    {bidder_text}
    
    Task: Extract 3 key mandatory criteria (Financial, Technical, Compliance) from the tender. 
    Check if the bidder meets them based on their submission.
    
    Return the result ONLY as a Markdown Table with columns: 
    Criterion | Requirement | Bidder Evidence | Status (Eligible/Ineligible/Review) | Confidence Score
    """)
    
    chain = prompt | llm
    response = chain.invoke({
        "tender_text": tender_text[:4000], # Simple clipping for demo context limits
        "bidder_text": bidder_text[:4000]
    })
    return response.content

# --- 3. UI Layout ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Step 1: Upload Tender")
    tender_file = st.file_uploader("Upload CRPF Tender (PDF)", type="pdf")

with col2:
    st.subheader("🏢 Step 2: Upload Bidder Docs")
    bidder_file = st.file_uploader("Upload Bidder Response (PDF)", type="pdf")

if st.button("🚀 Run Eligibility Analysis"):
    if not api_key:
        st.error("Please provide an API key in the sidebar.")
    elif tender_file and bidder_file:
        with st.spinner("Analyzing documents for compliance..."):
            # Process PDFs
            t_text = extract_text_from_pdf(tender_file)
            b_text = extract_text_from_pdf(bidder_file)
            
            # Get AI Analysis
            result = analyze_compliance(t_text, b_text)
            
            st.divider()
            st.subheader("📊 Evaluation Report")
            st.markdown(result)
            
            st.success("Analysis Complete. Audit trail generated.")
    else:
        st.warning("Please upload both documents to proceed.")

# --- 4. Bharat Context Tip ---
st.sidebar.info("""
**Hackathon Tip:** To handle 'Scanned Photos' (a Non-Negotiable), 
integrate `pytesseract` or `EasyOCR` 
instead of just `pypdf`.
""")
