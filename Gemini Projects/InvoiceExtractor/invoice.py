from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")



st.set_page_config(page_title = "Invoice Extractor")

st.header("End to End Multi Language Invoice Extractor Project using Gemini Pro LLM Model")
input =  st.text_input("input ", key = "input")
uploaded_file = st.file_uploader("upload invoice image", type = ["jpg", "png", "jpeg"])
image = ""

if uploaded_file is not None:
    image =  Image.open(uploaded_file)
    st.image(image, caption = "upload image", use_column_width=True)
    
submit = st.button("tell me about the invoice")

input_prompt = """
You are an expert in understanding invoices. We will upload an image as an invoice, 
and you will have to answer any questions based on the uploaded invoice image.
"""
if submit:
    image_data = input_image_setup(uploaded_file)
    response = gemini_response(input_prompt,image_data,input)
    st.subheader("the response is ")
    st.write(response)