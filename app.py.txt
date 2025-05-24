import streamlit as st
from resume_utils import *

st.title("📄 Smart Resume Matcher")
st.write("Upload your resume and paste a job description to get your match score and suggestions.")

uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
job_description = st.text_area("Paste the Job Description here")

if uploaded_file and job_description:
    # Extract resume text
    if uploaded_file.name.endswith(".pdf"):
        resume_text = extract_text_from_pdf(uploaded_file)
    else:
        resume_text = extract_text_from_docx(uploaded_file)
    
    # Preprocess text
    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(job_description)
    
    # Extract keywords
    resume_keywords = extract_keywords(cleaned_resume)
    jd_keywords = extract_keywords(cleaned_jd)
    
    # Score and suggestions
    match_score = calculate_similarity(cleaned_resume, cleaned_jd)
    missing_keywords = find_missing_keywords(resume_keywords, jd_keywords)
    
    # Display results
    st.subheader("🔍 Match Score")
    st.metric(label="Resume vs Job Description", value=f"{match_score}%")

    st.subheader("🧩 Suggested Keywords to Add")
    if missing_keywords:
        st.write(", ".join(missing_keywords))
    else:
        st.success("Your resume already covers most keywords from the job description!")
