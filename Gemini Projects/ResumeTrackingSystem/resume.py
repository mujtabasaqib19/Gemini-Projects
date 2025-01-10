from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
import fitz  # PyMuPDF
import io
import base64

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_response(input, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

# Function to process uploaded PDF using PyMuPDF
def input_pdf(uploaded_file):
    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    first_page = pdf_document[0]  # Get the first page of the PDF

    pixmap = first_page.get_pixmap()

    img_byte_arr = io.BytesIO()
    img = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
    img.save(img_byte_arr, format="JPEG")
    img_byte_arr = img_byte_arr.getvalue()  # Get the byte array
    
    # Prepare the encoded data in the required format
    pdf_parts = [
        {
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_byte_arr).decode()  # Encode to base64 and decode to a string
        }
    ]
    return pdf_parts

# Streamlit App
st.set_page_config(page_title="ATS Resume")
st.header("Resume Application Tracking System (ATS) Using Google Gemini Pro Vision")

# Inputs
job_description = st.text_area("Job Description", key="input")
uploaded_file = st.file_uploader("Upload your resume in PDF format", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF uploaded successfully.")


s1 = st.button("Tell Me About the Resume")
s2 = st.button("Percentage match")

# Prompts
input_prompt1 = """
You are an experienced HR with tech experience in the field of Data Science, Full Stack Web Development, 
Big Data Engineering, DEVOPS, and Data Analysis. Your task is to review the provided resume 
against the job description for these profiles. 
Please share your professional evaluation on whether the candidate's profile aligns with the specified role. Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science, 
Web Development, Big Data Engineering, DEVOPS, Data Analysis, and deep ATS functionality. 
Your task is to evaluate the resume against the provided job description. 
Give me the percentage match of the resume with the job description. First, the output should come as a percentage, followed by the keywords missing and a professional evaluation.
"""

# Button Handlers
if s1:
    st.write("You clicked on Tell Me About the Resume")
    if uploaded_file is not None:
        pdf_content = input_pdf(uploaded_file)
        result = generate_response(job_description, pdf_content, input_prompt1)
        st.subheader("The response is:")
        st.write(result)
    else:
        st.write("Please upload the resume.")

elif s2:
    st.write("You clicked on Percentage match")
    if uploaded_file is not None:
        pdf_content = input_pdf(uploaded_file)
        result = generate_response(job_description, pdf_content, input_prompt2)
        st.subheader("The response is:")
        st.write(result)
    else:
        st.write("Please upload the resume.")

