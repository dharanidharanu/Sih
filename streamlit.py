import streamlit as st

# Title for the app
st.title("Interview Analysis Tool")

# User input: Discipline
discipline = st.text_input("Discipline")

# User input: Interview Board Subjects
subjects = st.text_input("Interview Board Subjects")

# File upload component
uploaded_file = st.file_uploader("Upload Files", type=["pdf", "docx", "txt"])

# Analyze button
if st.button("Analyze"):
    if uploaded_file is not None:
        # Process the file and perform analysis
        st.success("File uploaded successfully!")
        # Here you can add your analysis logic
        # For demonstration, I'm just showing the file name
        st.write("Uploaded file:", uploaded_file.name)

        # Displaying dummy expert scores
        st.subheader("Expert Scores")
        score1 = st.text_input("Score 1", "")
        score2 = st.text_input("Score 2", "")
        score3 = st.text_input("Score 3", "")

        # Display the entered expert scores
        st.write(f"Score 1: {score1}")
        st.write(f"Score 2: {score2}")
        st.write(f"Score 3: {score3}")

       
    else:
        st.error("Please upload a file before analyzing.")

# This can be replaced with actual expert score calculation or any other output
