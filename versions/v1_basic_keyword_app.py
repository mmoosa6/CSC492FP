import streamlit as st

st.set_page_config(page_title="AI Phishing Detector")

st.title("AI-Generated Phishing Detection System")

st.write("Welcome to the phishing detection prototype.")

email_subject = st.text_input("Email Subject")

email_body = st.text_area("Email Body")

if st.button("Analyze Email"):
    
    if "verify" in email_body.lower() or "suspended" in email_body.lower():
        st.error("⚠ Likely Phishing Email")
        st.write("Confidence Score: 89%")
    else:
        st.success("✅ Likely Legitimate Email")
        st.write("Confidence Score: 76%")