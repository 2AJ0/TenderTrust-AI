import streamlit as st
import pandas as pd
import time
from pypdf import PdfReader

st.set_page_config(page_title="TenderTrust AI", layout="wide")
st.title("🛡️ TenderTrust AI: CRPF Eligibility Engine")

# --- Mock Analysis Logic (No API Key Required) ---
def analyze_compliance_mock(tender_text, bidder_text):
    # Simulating AI processing time
    time.sleep(3) 
    
    # Static result for the demo to ensure it works without a key
    return """
    | Criterion | Requirement | Bidder Evidence | Status | Confidence |
    | :--- | :--- | :--- | :--- | :--- |
    | **Financial** | Min ₹5Cr Annual Turnover | Audit Report Page 4: Turnover is ₹5.2Cr | ✅ Eligible | 98% |
    | **Technical** | 3+ Years of Experience | Certificate Page 2: Operations since 2019 | ✅ Eligible | 95% |
    | **Compliance**| Valid GST Registration | GST Certificate found in Zip folder | ✅ Eligible | 92% |
    | **Certification**| ISO 9001:2015 | No ISO 9001 document detected in scan | ⚠️ Review | 40% |
    """

# --- UI Layout ---
st.sidebar.warning("🛠️ Demo Mode: Using Mock Analysis Engine (No API Key Required)")

col1, col2 = st.columns(2)
with col1:
    st.subheader("📋 Step 1: Upload Tender")
    tender_file = st.file_uploader("Upload CRPF Tender (PDF)", type="pdf")

with col2:
    st.subheader("🏢 Step 2: Upload Bidder Docs")
    bidder_file = st.file_uploader("Upload Bidder Response (PDF)", type="pdf")

if st.button("🚀 Run Eligibility Analysis"):
    if tender_file and bidder_file:
        with st.spinner("AI is analyzing documents for compliance..."):
            # Result from the mock engine
            result = analyze_compliance_mock("", "") 
            
            st.divider()
            st.subheader("📊 Automated Evaluation Report")
            st.markdown(result)
            st.success("Analysis Complete. Source-to-Verdict mapping generated.")
    else:
        st.warning("Please upload sample documents to see the analysis.")
