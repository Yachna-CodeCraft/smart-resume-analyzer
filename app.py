import streamlit as st

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

jd = st.text_area("Paste Job Description")

if st.button("Analyze"):
    st.write("Processing resume...")