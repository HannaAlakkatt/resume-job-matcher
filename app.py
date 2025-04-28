import streamlit as st
import PyPDF2
import re

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def calculate_match(resume_text, job_description_text):
    resume_words = set(re.findall(r'\w+', resume_text.lower()))
    job_description_words = set(re.findall(r'\w+', job_description_text.lower()))
    
    if not job_description_words:
        return 0

    matching_words = resume_words.intersection(job_description_words)
    match_percentage = (len(matching_words) / len(job_description_words)) * 100
    return round(match_percentage, 2)

st.title("📝 Resume to Job Description Matcher")

uploaded_resume = st.file_uploader("Upload your Resume (PDF)", type="pdf")
job_description = st.text_area("Paste the Job Description")

if uploaded_resume and job_description:
    resume_text = extract_text_from_pdf(uploaded_resume)
    match_percent = calculate_match(resume_text, job_description)
    st.subheader(f"🎯 Match Percentage: {match_percent}%")


