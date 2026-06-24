import streamlit as st

st.set_page_config(
    page_title="Secure Attendance System",
    page_icon="",
    layout="centered"
)

st.title("Secure Attendance System")
st.subheader("Phase 2 Local Setup Test")

st.write("Testing local Streamlit setup and browser camera input.")

image_file = st.camera_input("Take a test face photo")

if image_file is not None:
    st.image(image_file)
    st.success("Camera input works.")