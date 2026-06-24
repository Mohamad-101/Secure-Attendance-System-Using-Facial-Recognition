import streamlit as st

from src.database import init_db, get_users_count, get_face_profiles_count
from src.face_enrollment import enroll_user


st.set_page_config(
    page_title="Secure Attendance System",
    page_icon="📷",
    layout="centered",
)

init_db()

st.title("Secure Attendance System")
st.subheader("Phase 2: Face Enrollment Test")

student_id = st.text_input("Student ID")
full_name = st.text_input("Full Name")
email = st.text_input("Email Optional")
role = st.selectbox("Role", ["student", "teacher", "admin"])

input_method = st.radio(
    "Choose image input method",
    ["Camera", "Upload Image"]
)

image_file = None

if input_method == "Camera":
    image_file = st.camera_input("Take a clear face photo")
else:
    image_file = st.file_uploader(
        "Upload a clear face image",
        type=["jpg", "jpeg", "png"]
    )

if st.button("Enroll User"):
    try:
        result = enroll_user(
            student_id=student_id,
            full_name=full_name,
            email=email,
            role=role,
            image_file=image_file,
        )

        st.success("User enrolled successfully.")
        st.write(f"User ID: {result['user_id']}")
        st.write(f"Student ID: {result['student_id']}")
        st.write(f"Full Name: {result['full_name']}")
        st.write(f"Email: {result['email']}")
        st.write(f"Role: {result['role']}")

    except Exception as error:
        st.error(str(error))

st.divider()

st.subheader("Database Status")
st.write(f"Users count: {get_users_count()}")
st.write(f"Face profiles count: {get_face_profiles_count()}")