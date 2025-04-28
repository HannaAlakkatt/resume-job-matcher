import streamlit as st

def calculate_match(resume_text, job_description_text):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description_text.lower().split())
    if not job_words:
        return 0
    match_count = len(resume_words.intersection(job_words))
    match_percentage = (match_count / len(job_words)) * 100
    return round(match_percentage, 2)

st.title("Resume and Job Description Matcher")

resume_text = st.text_area("Paste your Resume Text Here")
job_description_text = st.text_area("Paste the Job Description Here")

if st.button("Check Match"):
    if resume_text and job_description_text:
        match = calculate_match(resume_text, job_description_text)
        st.success(f"Your resume matches {match}% of the job description!")
    else:
        st.error("Please paste both your resume and the job description.")





