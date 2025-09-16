import streamlit as st
from pdf_extracter import text_extractor
import google.generativeai as genai
import os 

# Configure trhe model 
key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key= key)
model = genai.GenerativeModel('gemini-2.5-flash-lite')
resume_text = job_desc = None

# upload resume 
st.sidebar.title(":orange[Upload your resume (pdf only)]")

file = st.sidebar.file_uploader('Resume', type=['pdf'])
if file:
        resume_text = text_extractor(file)
        # st.write(resume_text)
        
# let define the main page 
st.title(":orange[Skill Match] :blue[AI Assistant skill matching tool]")
st.markdown("#### This application will match your resume and the job description . It will create a detailed report on the match")
tips = ''' Follow these steps to proceed:
1. Upload your resume (pdf only).
2. Copy and past the job description for which you are applying for.
3. Click the button and see the magic 
'''

st.write(tips)

job_desc=st.text_area("Copy and Paste the Job Description here",max_chars=10000)

prompt=f'''
Assume you are expert in skill matching and creating profiles.
Match the following resume with the job description provided by the user.
Resume: {resume_text}
Job_Description: {job_desc}

Your output should be as follows:
* Give a brief description of the applicant in 3-5 lines.
* Give a range of expected ATS score along with the matching and non matching keywords.
* Give the chances of getting sorlisted for this position in percentage.
* perform SWOT analysis and discuss each and everything in bullets points
* Suggest what all improvement can be made in resume in order get better ats and increase percentage of getting shortlisted.
* Also create two customised resumes as per the job description provided and increase percentage of getting shortlisted.
* prepare one page resume in such a way that can be copied and converted in word and can be converted to pdf.
* use bullet points and table wherever required 
'''

button = st.button('Click')
if button:
    if resume_text and job_desc:
        response = model.generate_content(prompt)
        st.write(response.text)
    else:
        st.write("Please Upload your resume")