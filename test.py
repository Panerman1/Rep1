
from dotenv import load_dotenv
load_dotenv()
import streamlit as st 
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro-vision')

def main():
    st.title("Streamlit Sidebar Example")

    # Create a sidebar with options
    selected_option = st.sidebar.selectbox("Steps", ["Step 1", "Step 2"])

    # Display content based on the selected option
    if selected_option == "Step 1":
        st.title("Gemini Image Viewer")


        gemini_endpoint = 'YOUR_GEMINI_ENDPOINT'

         # Create GeminiImageLoader instance
        gemini_loader = GeminiImageLoader(api_key, gemini_endpoint)

        # Get user input for the keyword
        keyword = st.text_input("Enter a keyword to search for an image:")

        if keyword:
            # Load and display the image
            image_url = gemini_loader.get_image_url(keyword)
            if image_url:
            st.image(image_url, caption=f"Image related to '{keyword}'", use_column_width=True)
            else:
            st.warning("No image found for the given keyword.")

        if __name__ == "__main__":
            main()

        elif selected_option == "Step 2":
            st.write("This is the Settings page. Customize your app here.")

if __name__ == "__main__":
    main()
