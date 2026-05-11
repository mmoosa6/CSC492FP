# AI-Generated Phishing Detection System

This project implements a transformer-based phishing email detection prototype using Python, Streamlit, Hugging Face Transformers, and a phishing-focused BERT model.

The application allows a user to enter an email subject and body. The system analyzes the text and classifies the message as either phishing or legitimate communication. It also displays a confidence score, suspicious indicators, and an analysis history table.

## Features

- Streamlit web interface
- Transformer-based phishing detection
- Phishing-focused BERT model
- Confidence score display
- Suspicious indicator reporting
- Analysis history tracking

## Technologies Used

- Python 3.12
- Streamlit
- Hugging Face Transformers
- PyTorch
- pandas

## Model Used

Final model:

`ealvaradob/bert-finetuned-phishing`

Earlier prototype model:

`facebook/bart-large-mnli`

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Development Versions

Earlier prototype versions are included in the `versions` folder to demonstrate the iterative refinement process throughout implementation.

## Project Purpose

This project was developed as a senior design project to explore how transformer-based natural language processing can help detect AI-generated phishing emails.