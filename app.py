import streamlit as st
import PyPDF2

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def calculate_match(resume_text, job_description_text):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description_text.lower().split())
    if not job_words:
        return 0
    match_count = len(resume_words.intersection(job_words))
    match_percentage = (match_count / len(job_words)) * 100
    return round(match_percentage, 2)

st.title("Resume and Job Description Matcher (with PDF Upload)")

uploaded_resume = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_description_text = st.text_area("Paste the Job Description Here")

if st.button("Check Match"):
    if uploaded_resume is not None and job_description_text:
        resume_text = extract_text_from_pdf(uploaded_resume)
        match = calculate_match(resume_text, job_description_text)
        st.success(f"Your resume matches {match}% of the job description!")
    else:
        st.error("Please upload your resume and paste the job description.")






