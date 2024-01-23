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
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{
            'mime_type':uploaded_file.type,
            'data':bytes_data
        }]
        return image_parts
    else:
        raise FileNotFoundError('No file Uploaded')
st.header('BASIC GEO-LOCATION DESCRIBER!!!')
input = st.text_input('Additional questions:',key = 'input')
uploaded_file = st.file_uploader('Image of the location:', type = ['jpg','jpeg','png'])

sub = st.button('Tell me about this location:')

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Upload File", use_column_width = True)
    
input_prompt =   """Under the title -'LOCATION AND BASIC INFO :-' , You have to identify the following :- (the name of the location (if it is a popular location), name of the structure (if it has a name), the state it is located in, country of the place in the image that is provided). Also describe few key features about the location in the image.              
                    After giving the  output , display the title 'ANSWER TO ADDITIONAL QUESTIONS ( If Any) :-' """

if sub:
    with st.spinner('Wait'):
        image_data = input_image_details(uploaded_file)
        response = get_gemini_response(input_prompt,image_data,input)
        st.header('Most probable answer:')
        st.text_area(label="",value= response,height=500)
