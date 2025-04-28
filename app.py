import streamlit as st

st.title("Resume and Job Description Matcher")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

job_description = st.text_area("Paste the Job Description here")

if uploaded_file is not None and job_description:
    st.success("Resume and Job Description uploaded!")


    st.subheader("Match Percentage:")
    st.write("🔵 75% match!") 
