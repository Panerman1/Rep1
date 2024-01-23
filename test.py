from dotenv import load_dotenv
load_dotenv()
import streamlit as st 
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input , image_date, user_prompt):
    response = model.generate_content([input,image_date[0],user_prompt])
    return response.text
