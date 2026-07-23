import hashlib

import pandas as pd
import streamlit as st

from src.database import (
    init_db,
    get_users_count,
    get_face_profiles_count,
    get_attendance_logs_count,
    get_attendance_logs,
)
from src.face_enrollment import enroll_user
from src.face_verification import verify_face
from src.attendance import mark_attendance


st.set_page_config(
    page_title="Secure Attendance System",
    page_icon="📷",
    layout="wide",
)

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            max-width: 1200px;
        }

        h1 {
            margin-bottom: 0.2rem;
        }

        h2, h3 {
            margin-top: 0.4rem;
            margin-bottom: 0.4rem;
        }

        div[data-testid="stVerticalBlock"] {
            gap: 0.55rem;
        }

        section[data-testid="stSidebar"] {
            width: 260px !important;
        }

        .small-note {
            color: #777;
            font-size: 0.9rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

init_db()

st.title("Secure Attendance System")
st.caption("Face Enrollment, Verification, and Attendance Logging")


menu = st.sidebar.radio(
    "Navigation",
    [
        "Register User",
        "Verify Attendance",
        "View Attendance Logs",
        "Database Status",
    ],
)


def get_face_input(key_prefix: str):
    input_method = st.radio(
        "Image input method",
        ["Camera", "Upload Image"],
        horizontal=True,
        key=f"{key_prefix}_input_method",
    )

    if input_method == "Camera":
        return st.camera_input(
            "Take a clear face photo",
            key=f"{key_prefix}_camera",
        )

    return st.file_uploader(
        "Upload a clear face image",
        type=["jpg", "jpeg", "png"],
        key=f"{key_prefix}_upload",
    )


if menu == "Register User":
    st.header("Register User")

    left_col, right_col = st.columns([1, 1.2], vertical_alignment="top")

    with left_col:
        st.subheader("User Information")

        student_id = st.text_input("Student ID", placeholder="Example: S001")
        full_name = st.text_input("Full Name", placeholder="Enter full name")
        email = st.text_input("Email Optional", placeholder="example@email.com")
        role = st.selectbox("Role", ["student", "teacher", "admin"])

        enroll_button = st.button(
            "Enroll User",
            use_container_width=True,
        )

    with right_col:
        st.subheader("Face Image")
        st.caption("Use a clear image with one visible face.")
        image_file = get_face_input("register")

    if enroll_button:
        try:
            result = enroll_user(
                student_id=student_id,
                full_name=full_name,
                email=email,
                role=role,
                image_file=image_file,
            )

            with left_col:
                st.success("User enrolled successfully.")
                st.write(f"**User ID:** {result['user_id']}")
                st.write(f"**Student ID:** {result['student_id']}")
                st.write(f"**Full Name:** {result['full_name']}")
                st.write(f"**Email:** {result['email']}")
                st.write(f"**Role:** {result['role']}")

        except Exception as error:
            with left_col:
                st.error(str(error))


elif menu == "Verify Attendance":
    st.header("Verify Attendance")

    left_col, right_col = st.columns([1, 1.2], vertical_alignment="top")

    with left_col:
        st.subheader("Verification Panel")

        st.write(
            "Take or upload a face image. The system will automatically verify "
            "the user and record attendance."
        )

        tolerance = st.slider(
            "Recognition tolerance",
            min_value=0.3,
            max_value=0.8,
            value=0.6,
            step=0.05,
        )

        result_area = st.container()

    with right_col:
        st.subheader("Face Image")
        st.caption("Use a clear, front-facing image.")
        image_file = get_face_input("verify")

    if image_file is None:
        with result_area:
            st.info("Waiting for a face image.")

    else:
        image_bytes = image_file.getvalue()
        image_hash = hashlib.sha256(image_bytes).hexdigest()

        with result_area:
            if st.session_state.get("last_verified_image_hash") == image_hash:
                st.info(
                    "This image has already been processed. "
                    "Take or upload a new image to verify again."
                )

            else:
                st.session_state["last_verified_image_hash"] = image_hash

                try:
                    image_file.seek(0)

                    with st.spinner("Verifying face and recording attendance..."):
                        verification_result = verify_face(
                            image_file=image_file,
                            tolerance=tolerance,
                        )

                    if not verification_result["matched"]:
                        st.error(verification_result["message"])
                        st.write(f"**Best Distance:** {verification_result['distance']:.4f}")

                    else:
                        st.success("Face verified successfully.")

                        st.write(f"**Student ID:** {verification_result['student_id']}")
                        st.write(f"**Full Name:** {verification_result['full_name']}")
                        st.write(f"**Email:** {verification_result['email']}")
                        st.write(f"**Role:** {verification_result['role']}")
                        st.write(f"**Face Distance:** {verification_result['distance']:.4f}")

                        attendance_result = mark_attendance(
                            user_id=verification_result["user_id"],
                            face_distance=verification_result["distance"],
                        )

                        if attendance_result["recorded"]:
                            st.success(attendance_result["message"])
                        else:
                            st.warning(attendance_result["message"])

                except Exception as error:
                    st.error(str(error))


elif menu == "View Attendance Logs":
    st.header("Attendance Logs")

    logs = get_attendance_logs()

    if not logs:
        st.info("No attendance logs found yet.")
    else:
        df = pd.DataFrame(logs)

        st.dataframe(
            df,
            use_container_width=True,
            height=430,
        )

        csv_data = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Attendance Logs as CSV",
            data=csv_data,
            file_name="attendance_logs.csv",
            mime="text/csv",
            use_container_width=True,
        )


elif menu == "Database Status":
    st.header("Database Status")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Registered Users", get_users_count())

    with col2:
        st.metric("Face Profiles", get_face_profiles_count())

    with col3:
        st.metric("Attendance Logs", get_attendance_logs_count())

    st.divider()

    st.info(
        "This page only shows system statistics. "
        "Local database files and biometric data should not be uploaded to GitHub."
    )