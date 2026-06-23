import streamlit as st

st.set_page_config(
    page_title="Seller Onboarding Agent",
    page_icon="📄"
)

st.title("📄 Seller Onboarding Agent")

seller_name = st.text_input("Seller Name")

uploaded_files = st.file_uploader(
    "Upload Documents",
    accept_multiple_files=True
)

if st.button("Submit"):
    st.success("Documents uploaded successfully!")

if uploaded_files:
    st.subheader("Uploaded Files")

    for file in uploaded_files:
        st.write(f"✅ {file.name}")
