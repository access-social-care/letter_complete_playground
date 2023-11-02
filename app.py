import streamlit as st

# Create a choicebox to select "first" or "second"
choice = st.selectbox("Choose:", ("", "first", "second"))

# Define the file name based on the choice
file_name = f"{choice}.txt"

# Function to read and display the content of the selected text file
def read_and_display_text(file_name):
    try:
        with open(file_name, "r") as file:
            file_content = file.read()
            st.text("File Content:")
            st.text(file_content)
    except FileNotFoundError:
        st.text("Please select a valid file")

# Call the function to read and display the text file
read_and_display_text(file_name)

