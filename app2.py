import streamlit as st
import sys

# Get the URL parameter
file_choice = st.experimental_get_query_params()
if file_choice:
    choice = file_choice.get("file", [""])[0]
else:
    choice = ""

# Define the file name based on the URL parameter
file_name = f"{choice}.txt"

# Function to read and display the content of the selected text file
def read_and_display_text(file_name):
    try:
        with open(file_name, "r") as file:
            file_content = file.read()
            st.text("File Content:")
            st.text(file_content)
    except FileNotFoundError:
        st.text("File not found.")

# Call the function to read and display the text file
read_and_display_text(file_name)

