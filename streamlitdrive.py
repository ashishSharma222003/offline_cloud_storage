import streamlit as st
import os

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

st.title('File Upload App')

uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv", "png", "jpg", "jpeg", "pdf", "mp4", "avi", "mov", "mkv"])

if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")

st.subheader('Existing Files')

file_list = os.listdir(UPLOAD_DIR)
if file_list:
    for file_name in file_list:
        file_path = os.path.join(UPLOAD_DIR, file_name)
        # Create a download button for each file
        with open(file_path, "rb") as file:
            st.download_button(
                label=f"Download {file_name}",
                data=file,
                file_name=file_name
            )
else:
    st.write("No files found.")
