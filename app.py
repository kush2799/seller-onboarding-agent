import streamlit as st

st.set_page_config(
    page_title="Seller Onboarding Agent",
    page_icon="📄"
)

st.title("📄 Seller Onboarding Agent")

seller_name = st.text_input("Seller Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")

uploaded_files = st.file_uploader(
    "Upload Documents",
    accept_multiple_files=True
)

if st.button("Submit"):

    st.success("Application Submitted")

    st.write("### Summary")
    st.write("Seller:", seller_name)
    st.write("Email:", email)
    st.write("Phone:", phone)

    if uploaded_files:
        st.write("### Uploaded Documents")

        for file in uploaded_files:
            st.write(f"✅ {file.name}")
