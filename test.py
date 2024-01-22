import streamlit as st
import requests

class GeminiImageLoader:
    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        self.endpoint = endpoint

    def get_image_url(self, keyword):
        # Make a request to the Gemini API to get the image URL based on the keyword
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}',
        }

        payload = {
            'keyword': keyword,
            # Add any other required parameters for image retrieval
        }

        response = requests.post(self.endpoint, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            return result.get('image_url')
        else:
            st.error(f"Error: {response.status_code}, {response.text}")
            return None

def main():
    st.title("Gemini Image Viewer")

    # Get Gemini API key and endpoint
    api_key = 'YOUR_API_KEY'
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
