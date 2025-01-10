from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the GenerativeModel
model = genai.GenerativeModel("gemini-1.5-flash")

# Define a function for getting a response from the Gemini model
def gemini_response(input_text, image):
    if input_text!="":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title='Image Model')
st.header("Building End-to-End LLM and Large Image Model Application Using Gemini Pro")

input_text = st.text_input("Input: ", key="input")

uploaded_file = st.file_uploader("Choose an image.", type=["jpg", "jpeg", "png"])
image = "" 

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

if st.button("Tell me about the image"):
    if image is not None:
        try:
            response = gemini_response(input_text, image)
            st.subheader("The response is:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred while processing the request: {e}")
    else:
        st.warning("Please upload an image to proceed.")
