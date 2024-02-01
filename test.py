import streamlit as st
import base64
import os

def main():
    st.title("Binary File Download Example")

    # Upload binary file
    uploaded_file = st.file_uploader("Choose a binary file", type=("jpg", "png", "jpeg", "pdf", "zip"))

    if uploaded_file is not None:
        # Display the file information
        file_info = f"File Name: {uploaded_file.name}, File Size: {uploaded_file.size} bytes"
        st.write(file_info)

        # Create a download link
        download_link = create_download_link(uploaded_file, "Download File")
        st.markdown(download_link, unsafe_allow_html=True)

def create_download_link(uploaded_file, link_text):
    """Generate a download link for the given file."""
    with open(uploaded_file.name, "wb") as file:
        file.write(uploaded_file.read())
    
    with open(uploaded_file.name, "rb") as file:
        file_content = file.read()
        b64 = base64.b64encode(file_content).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="{uploaded_file.name}">{link_text}</a>'
    
    # Remove the temporary file
    os.remove(uploaded_file.name)

    return href

if __name__ == "__main__":
    main()
