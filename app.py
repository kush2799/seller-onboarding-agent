import streamlit as st
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(
    page_title="Seller Onboarding Agent",
    page_icon="📄"
)

st.title("📄 Seller Onboarding Agent")

uploaded_file = st.file_uploader(
    "Upload GST Certificate / PAN / Business Document",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:

    st.write("File Name:", uploaded_file.name)
    st.write("File Type:", uploaded_file.type)

    st.success("Document Uploaded")

    if st.button("Extract Details"):

        try:
            # Use latest available model
            model = genai.GenerativeModel("gemini-2.0-flash")

            response = model.generate_content("Hello")

            st.success("Gemini Connected!")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {str(e)}")
