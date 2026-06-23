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

    st.success("Document Uploaded")

    if st.button("Extract Details"):

        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
    
            response = model.generate_content(
                "Hello"
            )
    
            st.success("Gemini Connected!")
            st.write(response.text)
    
        except Exception as e:
            st.error(str(e))
