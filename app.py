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
    page_icon="",
    layout="centered",
)

init_db()

st.title("Secure Attendance System")
st.write("Face Enrollment, Verification, and Attendance Logging")


menu = st.sidebar.radio(
    "Menu",
    [
        "Register User",
        "Verify Attendance",
        "View Attendance Logs",
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


elif menu == "Verify Attendance":
    st.header("Verify Attendance")

    st.write(
        "Take or upload a face image. The system will automatically verify the face "
        "and record attendance."
    )

    image_file = get_face_input("verify")

    tolerance = st.slider(
        "Recognition tolerance",
        min_value=0.3,
        max_value=0.8,
        value=0.6,
        step=0.05,
    )

    if image_file is not None:
        image_bytes = image_file.getvalue()
        image_hash = hashlib.sha256(image_bytes).hexdigest()

        if st.session_state.get("last_verified_image_hash") != image_hash:
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
                        st.write(f"Best Distance: {verification_result['distance']:.4f}")

                    else:
                        st.success("Face verified successfully.")
                        st.write(f"Student ID: {verification_result['student_id']}")
                        st.write(f"Full Name: {verification_result['full_name']}")
                        st.write(f"Email: {verification_result['email']}")
                        st.write(f"Role: {verification_result['role']}")
                        st.write(f"Face Distance: {verification_result['distance']:.4f}")

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

        else:
            st.info(
                "This image has already been processed. "
                "Take or upload a new image to verify again."
            )


elif menu == "View Attendance Logs":
    st.header("Attendance Logs")

    logs = get_attendance_logs()

    if not logs:
        st.info("No attendance logs found yet.")
    else:
        df = pd.DataFrame(logs)

        if "attendance_date" in df.columns:
            df["attendance_date"] = pd.to_datetime(
                df["attendance_date"],
                errors="coerce"
            ).dt.date

        st.subheader("Filters")

        filter_col1, filter_col2, filter_col3 = st.columns(3)

        with filter_col1:
            search_query = st.text_input(
                "Search by Student ID or Name",
                placeholder="Example: S001 or Mohamad",
            )

        with filter_col2:
            available_dates = sorted(df["attendance_date"].dropna().unique())

            if available_dates:
                default_start_date = available_dates[0]
                default_end_date = available_dates[-1]
            else:
                default_start_date = None
                default_end_date = None

            date_range = st.date_input(
                "Filter by Date Range",
                value=(default_start_date, default_end_date)
                if default_start_date and default_end_date
                else None,
            )

        with filter_col3:
            status_options = sorted(df["status"].dropna().unique().tolist())

            selected_status = st.multiselect(
                "Filter by Status",
                options=status_options,
                default=status_options,
            )

        filtered_df = df.copy()

        if search_query:
            search_query = search_query.lower().strip()

            filtered_df = filtered_df[
                filtered_df["student_id"].astype(str).str.lower().str.contains(search_query)
                | filtered_df["full_name"].astype(str).str.lower().str.contains(search_query)
            ]

        if date_range and len(date_range) == 2:
            start_date, end_date = date_range

            filtered_df = filtered_df[
                (filtered_df["attendance_date"] >= start_date)
                & (filtered_df["attendance_date"] <= end_date)
            ]

        if selected_status:
            filtered_df = filtered_df[
                filtered_df["status"].isin(selected_status)
            ]

        st.subheader("Summary")

        metric_col1, metric_col2, metric_col3 = st.columns(3)

        with metric_col1:
            st.metric("Total Records", len(filtered_df))

        with metric_col2:
            if "student_id" in filtered_df.columns:
                st.metric("Unique Students", filtered_df["student_id"].nunique())
            else:
                st.metric("Unique Students", 0)

        with metric_col3:
            if "attendance_date" in filtered_df.columns:
                st.metric("Attendance Days", filtered_df["attendance_date"].nunique())
            else:
                st.metric("Attendance Days", 0)

        st.subheader("Filtered Attendance Records")

        if filtered_df.empty:
            st.warning("No records match the selected filters.")
        else:
            st.dataframe(
                filtered_df,
                use_container_width=True,
                height=420,
            )

            csv_data = filtered_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="Download Filtered Attendance Logs as CSV",
                data=csv_data,
                file_name="filtered_attendance_logs.csv",
                mime="text/csv",
                use_container_width=True,
            )


elif menu == "Database Status":
    st.header("Database Status")

    st.write(f"Users count: {get_users_count()}")
    st.write(f"Face profiles count: {get_face_profiles_count()}")
    st.write(f"Attendance logs count: {get_attendance_logs_count()}")