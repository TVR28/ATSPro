import pybase64
import io
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import PyPDF2 as pdf
import google.generativeai as genai
import time

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ''  # Ensure text is not None
    return text

## ------- Streamlit app setup ---------
st.set_page_config(page_title="ATSPro", page_icon="📑", layout = 'wide')

with open( "styles/main.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.title("ATSPro: The ATS-Conquering Companion")
st.subheader("Cross the ATS Hurdle: Unlock Your Career Potential with Precision and Insight")

#Set BAckground Image
def set_bg_image(image_file):
    with open(image_file, "rb") as file:
        # Use base64 to encode the image file
        encoded_image = pybase64.b64encode(file.read()).decode()

    # Set the background using CSS styles
    css_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """

    st.markdown(css_style, unsafe_allow_html=True)

set_bg_image("background.JPG")

st.write("""_**ATSPro**_ is your strategic ally in mastering the **Applicant Tracking System (ATS)** challenge, powered by the advanced capabilities of _**Google Gemini Pro**_. This ATS Expert System is crafted to refine and align your resume with precision, ensuring it resonates with both the ATS algorithms and human recruiters' expectations.

Through a deep analysis of your resume against specific job descriptions, _**ATSPro**_ identifies key areas for enhancement, from keyword optimization to structural improvements, making your application ATS-friendly. Our unique feature set also includes generating custom interview questions and answers, tailored to your resume and the job you're targeting, ensuring you're well-prepared for both technical and HR evaluations.""")

# Role input

role = st.text_input("**What's the Job Role?**", 'Machine Learning Engineer')


if role is not '':
    st.write(f":black[You entered **{role}** as your role.]")
else:
    st.write("Enter a Job Role")



# Initialize session state variables for button clicks
if 'submit1_clicked' not in st.session_state:
    st.session_state['submit1_clicked'] = False
if 'submit2_clicked' not in st.session_state:
    st.session_state['submit2_clicked'] = False
if 'submit3_clicked' not in st.session_state:
    st.session_state['submit3_clicked'] = False
if 'submit4_clicked' not in st.session_state:
    st.session_state['submit4_clicked'] = False
if 'submit5_clicked' not in st.session_state:
    st.session_state['submit5_clicked'] = False

# Define button click callbacks to set state
def on_submit1_clicked():
    st.session_state['submit1_clicked'] = True

def on_submit2_clicked():
    st.session_state['submit2_clicked'] = True

def on_submit3_clicked():
    st.session_state['submit3_clicked'] = True

def on_submit4_clicked():
    st.session_state['submit4_clicked'] = True

def on_submit5_clicked():
    st.session_state['submit5_clicked'] = True

# Job description and resume upload
jd = st.text_area("**Paste the Job Description**")
uploaded_file = st.file_uploader("**Upload Your Resume**", type="pdf", help="Please upload a pdf")

col1, col2, col3, col4, col5 = st.columns(5)

# Display buttons and check their state
with col1:
    submit1 = st.button("Tell Me About My Resume", on_click=on_submit1_clicked,type="primary")
with col2:
    submit2 = st.button("Percentage(%) Match ", on_click=on_submit2_clicked,type="primary")
with col3:
    submit3 = st.button("How to Improve Skills", on_click=on_submit3_clicked,type="primary")
with col4:
    submit4 = st.button("Customization Tips", on_click=on_submit4_clicked,type="primary")
with col5:
    submit5 = st.button("Interview Prep Guide", on_click=on_submit5_clicked,type="primary")

# Process button clicks
if submit1 and st.session_state['submit1_clicked']:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        prompt1 = f"""
        You are a professional and experienced ATS(Application Tracking System) with a deep understanding of {role} fields. Analyze the provided resume and job description (JD). Provide a detailed analysis (200-300 words) of how the resume aligns with the JD, highlighting key areas of strength, relevant experiences, and qualifications. Discuss any notable achievements or skills that are particularly well-matched to the job requirements.
        
        Here is the resume content : {text}
        Here is the job description : {jd}
        Your Response Should have the following structure
        Example:
        
        Note: Only Mention and Analyze the content of the provided resume text. Make sure Nothing additional is added outside the provided text 
        
        Resume Analysis and Alignment with Job Description:

        Overview: 
        The resume presents a strong background in software engineering, with a particular emphasis on full-stack development and cloud technologies.
        
        Strengths:
        - Technical Proficiency: Proficient in key programming languages such as Python, JavaScript, and Java, aligning well with the job's technical requirements.
        - Project Experience: Showcases several projects that demonstrate the ability to design, develop, and deploy scalable software solutions, mirroring the JD's emphasis on hands-on experience.
        
        Relevant Experiences: (Highlight only the things that are present in the resume.)
        - Lead Developer Role: Led a team in developing a SaaS application using microservices architecture, directly relevant to the job's focus on leadership and microservices.
        - Cloud Solutions Architect: Experience in designing cloud infrastructure on AWS, aligning with the JD's requirement for cloud computing skills.
        
        """

        response = get_gemini_response(prompt1)
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.write(response)  # Use st.write to display the response

if submit2 and st.session_state['submit2_clicked']:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        prompt2 = f"""
        You are a professional and experienced ATS(Application Tracking System) with a deep understanding of {role} fields. Evaluate the resume strictly based on the provided job description and resume content. Identify and list the keywords and phrases that match between the resume and the JD. Highlight any missing keywords or skills crucial for the job but not present in the resume. Provide a percentage match based on the analysis.
        
        Here is the resume content : {text}
        Here is the job description : {jd}
        
        Your Response Should have the following ouput structure
        Note: strictly Mention and Analyze only the content of the provided resume text. Make sure Nothing additional is added outside the provided text.
        
        Output Structure:
        Percentage Match: [Provide percentage]

        Matched Keywords:

        Skills: [List matched skills]
        Technologies: [List matched technologies]
        Methodologies: [List matched methodologies]
        
        Missing Keywords: [List missing skills or technologies crucial for the role but not found in the resume]

        Final Thoughts: [Provide a brief assessment of the resume's alignment with the job requirements, mentioning areas of strength and opportunities for improvement.]
        """

        response = get_gemini_response(prompt2)
        st.subheader("Percentage Match Analysis")
        st.write(response)

if submit3 and st.session_state['submit3_clicked']:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        prompt3 = f"""
        You are a professional and experienced ATS(Application Tracking System) with a deep understanding of {role} fields. Based on the analysis of the resume and the job description, suggest specific improvements and additions to the candidate's skill set (200-300 words). Identify areas where the candidate falls short and recommend actionable steps or resources for acquiring or enhancing the necessary skills. Highlight the importance of these skills in the context of the targeted job role.
        
        Here is the resume content : {text}
        Here is the job description : {jd}
        Your Response Should have the following structure
        Example:
        
        Note: Only Mention and Analyze the content of the provided resume text. Make sure Nothing additional is added outside the provided text 
        
        Skills Improvement and Addition Suggestions:

        To further align your resume with the job requirements and the evolving trends in software engineering, consider the following improvements:

        Expand Knowledge in Emerging Technologies:
        - Dive into Machine Learning and Big Data Analytics; consider online courses or projects that demonstrate practical application.
        - Familiarize yourself with Blockchain Technology, given its growing impact on secure and decentralized systems.
        
        Enhance Cloud Computing Skills:
        - Gain deeper expertise in cloud services beyond AWS, such as Microsoft Azure or Google Cloud Platform, to showcase versatility.
        - Strengthen Soft Skills:
        Leadership and project management skills are highly valued; consider leading more projects or taking courses in Agile and Scrum methodologies.
        """

        response = get_gemini_response(prompt3)
        st.subheader("Skills Improvement Suggestions")
        st.write(response)

if submit4 and st.session_state['submit4_clicked']:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        prompt4 = f"""
        You are a professional and experienced ATS(Application Tracking System) with a deep understanding of {role} fields. Review the resume's bullet points in light of the job description. Provide targeted suggestions on how to edit existing bullet points to better align with the job requirements. Focus on enhancing clarity, relevance, and impact by incorporating keywords from the JD and emphasizing achievements and skills that are most pertinent to the job.
        
        Here is the resume content : {text}
        Here is the job description : {jd}
        Your Response Should have the following structure
        Example:
        
        Note: Only Mention and Analyze the content of the provided resume text. Make sure Nothing additional is added outside the provided text 
        
        Resume Customization Tips for Better Alignment with Job Description:

        Tailor Bullet Points:
        - Current: "Developed a web application using React and Node.js."
        - Revised: "Engineered a scalable web application using React and Node.js, incorporating microservices architecture to enhance modularity and deployability, directly supporting team objectives in agile development environments."
        
        Highlight Specific Achievements:
        - Current: "Designed cloud infrastructure for various projects."
        - Revised: "Strategically designed and deployed robust cloud infrastructure on AWS for 3 enterprise-level projects, achieving a 20% improvement in deployment efficiency and cost reduction."
        
        Incorporate Missing Keywords:
        If you have experience with Machine Learning, add a bullet point like: "Implemented machine learning    algorithms to automate data processing tasks, resulting in a 30% reduction in processing times."
        """

        response = get_gemini_response(prompt4)
        st.subheader("Customization Tips")
        st.write(response)

if submit5 and st.session_state['submit5_clicked']:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        prompt5 = f"""
        You are a professional and experienced ATS(Application Tracking System) with a deep understanding of {role} fields. Analyze the provided resume and job description (JD). Generate a set of interview questions and suggested answers tailored to this specific context. The questions should be designed to explore the candidate's technical skills, experiences, and personal attributes relevant to the role, as described in the JD and evidenced in the resume. Provide 5 technical interview questions (1 easy question, 2 medium questions, 3 hard questions) focusing on the key skills and technologies mentioned in the JD and resume. The technical questions should sound specific and technical. Additionally, provide 5 HR interview questions (1 easy question, 2 medium questions, 3 hard questions) that probe into the candidate's behavioral traits, problem-solving abilities, and cultural fit for the organization. For each question, include a detailed sample answer that highlights how the candidate can effectively showcase their relevant skills, experiences, and achievements from their resume in response to the job requirements outlined in the JD."

        Here is the resume content : {text}
        Here is the job description : {jd}
        Instructions for Response:

        Technical Questions:
        Create questions that are directly related to the technical skills and experiences mentioned in the JD and resume.
        Ensure questions cover a range of difficulties (easy, medium, hard) and are relevant to real-world scenarios the candidate might face in the role.
        
        HR Questions:
        Formulate questions that assess cultural fit, teamwork, leadership, and resilience.
        Questions should invite responses that allow the candidate to demonstrate their problem-solving approach, adaptability, and growth mindset.
        
        Suggested Answers:
        Provide comprehensive sample answers for each question, guiding the candidate on how to integrate their specific experiences and achievements from the resume.
        Highlight how each answer can align with the expectations set forth in the JD, showcasing the candidate's suitability for the role.
        
        Your Response Should have the following structure
        
        Technical Interview Questions:
        
        Question1: (Question here)
        Answer1: (Answer here)
        
        Similarly all other questions.
        
        HR Interview Questions:
        
        Question1: (Question here)
        Answer1: (Answer here)
        
        Similarly all other questions.
        """

        response = get_gemini_response(prompt5)
        st.subheader("Interview Preperation Guide ")
        st.write("Here are some sample Technical and HR interview questions which will help you in answering different questions faced in the interviews.")
        st.write(response)
