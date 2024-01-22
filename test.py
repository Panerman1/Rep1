import streamlit as st

def home_page():
    st.title("Home Page")
    st.write("Welcome to the Home page!")

def about_page():
    st.title("About Page")
    st.write("This is the About page. Learn more about the app here.")

def main():
    st.sidebar.title("Navigation")
    pages = st.sidebar.multiselect("Select pages", ["Home", "About"])

    if "Home" in pages:
        home_page()
    
    if "About" in pages:
        about_page()

if __name__ == "__main__":
    main()
