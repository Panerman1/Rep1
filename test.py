import streamlit as st

def main():
    st.title("Streamlit Sidebar Example")

    # Create a sidebar with options
    selected_option = st.sidebar.selectbox("Select an option", ["Home", "Settings", "About"])

    # Display content based on the selected option
    if selected_option == "Home":
        st.write("Welcome to the Home page!")
    elif selected_option == "Settings":
        st.write("This is the Settings page. Customize your app here.")
    elif selected_option == "About":
        st.write("Learn more about this app on the About page.")

if __name__ == "__main__":
    main()
