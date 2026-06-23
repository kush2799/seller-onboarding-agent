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

        file_bytes = uploaded_file.getvalue()

        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = """
        Extract the following details from this document.

        Return ONLY in this format:

        Company Name:
        GST Number:
        PAN Number:
        Address:

        If any field is unavailable, write Not Found.
        """

        response = model.generate_content(
            [
                prompt,
                {
                    "mime_type": uploaded_file.type,
                    "data": file_bytes
                }
            ]
        )

        st.subheader("Extracted Details")

        st.write(response.text)
