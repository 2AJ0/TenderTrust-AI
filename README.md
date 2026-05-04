# 🛡️ TenderTrust AI: CRPF Eligibility Engine

**TenderTrust AI** is an automated compliance platform designed for the **AI for Bharat Hackathon (Theme 3)**. It streamlines the evaluation of government tenders for the CRPF by using Multi-Modal AI to cross-reference tender requirements against complex, unstructured bidder submissions.

## ✨ Key Features
- **Smart Criteria Extraction:** Automatically identifies Mandatory vs. Optional criteria (Financial, Technical, Compliance) from Tender PDFs.
- **Multi-Modal OCR:** Handles typed PDFs, scanned certificates, and mobile photographs of documents.
- **Source-to-Verdict Transparency:** Every "Eligible" or "Ineligible" status includes a direct reference/quote from the source document.
- **Human-in-the-Loop (HITL):** Low-confidence matches are flagged for manual officer review to prevent silent disqualification.

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **LLM Orchestration:** LangChain / GPT-4o
- **Document Processing:** PyPDF & OCR (LayoutLM integration ready)
- **Data Privacy:** Designed for local embedding execution to protect sensitive PII.

### Prerequisites
- Python 3.9+
- OpenAI API Key (or local LLM environment)

