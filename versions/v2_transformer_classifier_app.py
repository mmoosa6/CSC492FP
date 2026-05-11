import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Phishing Detector")

st.title("AI-Generated Phishing Detection System")

st.write("Transformer-Based Email Classification Prototype")

@st.cache_resource
def load_classifier():
    return pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli",
        device=-1
    )

classifier = load_classifier()

email_subject = st.text_input("Email Subject")

email_body = st.text_area("Email Body")

if st.button("Analyze Email"):

    email_text = email_subject + " " + email_body

    labels = ["phishing", "legitimate"]

    result = classifier(email_text, labels)

    prediction = result["labels"][0]
    confidence = result["scores"][0]

    if prediction == "phishing":
        st.error(f"⚠ Likely Phishing Email ({confidence:.2%} confidence)")
    else:
        st.success(f"✅ Likely Legitimate Email ({confidence:.2%} confidence)")