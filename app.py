import streamlit as st

from src.database import (
    init_db,
    get_users_count,
    get_face_profiles_count,
)
from src.face_enrollment import enroll_user
from src.face_verification import verify_face


st.set_page_config(
    page_title="Secure Attendance System",
    page_icon="",
    layout="centered",
)

init_db()

st.title("Secure Attendance System")
st.write("Phase 2 MVP: Enrollment and Face Verification")


menu = st.sidebar.radio(
    "Menu",
    [
        "Register User",
        "Verify Face",
        "Database Status",
    ],
)


def get_face_input(key_prefix: str):
    input_method = st.radio(
        "Choose image input method",
        ["Camera", "Upload Image"],
        key=f"{key_prefix}_input_method",
    )

    image_file = None

    if input_method == "Camera":
        image_file = st.camera_input(
            "Take a clear face photo",
            key=f"{key_prefix}_camera",
        )
    else:
        image_file = st.file_uploader(
            "Upload a clear face image",
            type=["jpg", "jpeg", "png"],
            key=f"{key_prefix}_upload",
        )

    return image_file


if menu == "Register User":
    st.header("Register User")

    student_id = st.text_input("Student ID")
    full_name = st.text_input("Full Name")
    email = st.text_input("Email Optional")
    role = st.selectbox("Role", ["student", "teacher", "admin"])

    image_file = get_face_input("register")

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


elif menu == "Verify Face":
    st.header("Verify Face")

    st.write("Take or upload a new face image to compare it with enrolled users.")

    image_file = get_face_input("verify")

    tolerance = st.slider(
        "Recognition tolerance",
        min_value=0.3,
        max_value=0.8,
        value=0.6,
        step=0.05,
    )

    if st.button("Verify Face"):
        try:
            result = verify_face(
                image_file=image_file,
                tolerance=tolerance,
            )

            if result["matched"]:
                st.success(result["message"])
                st.write(f"Student ID: {result['student_id']}")
                st.write(f"Full Name: {result['full_name']}")
                st.write(f"Email: {result['email']}")
                st.write(f"Role: {result['role']}")
                st.write(f"Face Distance: {result['distance']:.4f}")
            else:
                st.error(result["message"])
                st.write(f"Best Distance: {result['distance']:.4f}")

        except Exception as error:
            st.error(str(error))


elif menu == "Database Status":
    st.header("Database Status")

    st.write(f"Users count: {get_users_count()}")
    st.write(f"Face profiles count: {get_face_profiles_count()}")