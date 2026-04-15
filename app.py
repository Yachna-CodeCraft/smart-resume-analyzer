import streamlit as st
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])
jd = st.text_area("Paste Job Description")

def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

if st.button("Analyze"):
    if uploaded_file and jd:
        resume_text = extract_text(uploaded_file)

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume_text, jd])

        score = cosine_similarity(vectors[0], vectors[1])[0][0]

        st.success(f"Match Score: {round(score*100,2)}%")