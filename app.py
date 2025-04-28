import streamlit as st
import PyPDF2
import re
import time

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
    with st.spinner('Analyzing...'):
        time.sleep(2) 
        
        resume_text = extract_text_from_pdf(uploaded_resume)
        match_percent = calculate_match(resume_text, job_description)
        
        st.subheader(f"🎯 Match Percentage: {match_percent}%")

        progress_bar = st.progress(0)
        for percent_complete in range(int(match_percent) + 1):
            time.sleep(0.01)
            progress_bar.progress(percent_complete)

        if match_percent >= 80:
            st.balloons()

        if match_percent >= 80:
            st.success("Amazing match! 🚀 You are ready to apply!")
        elif match_percent >= 50:
            st.info("Good match, but consider tweaking your resume a bit!")
        else:
            st.warning("Low match. You might want to tailor your resume more carefully.")




