import hashlib

import pandas as pd
import streamlit as st

from src.database import (
    init_db,
    get_users_count,
    get_face_profiles_count,
    get_attendance_logs_count,
    get_attendance_logs,
    log_security_event,
    get_security_logs,
    get_security_logs_count,
)
from src.face_enrollment import enroll_user
from src.face_verification import verify_face
from src.attendance import mark_attendance
from src.access_control import require_admin_access


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
    </style>
    """,
    unsafe_allow_html=True,
)


init_db()

st.title("Secure Attendance System")
st.caption("Face Enrollment, Verification, Attendance Logging, and Security Monitoring")


menu = st.sidebar.radio(
    "Navigation",
    [
        "Register User",
        "Verify Attendance",
        "View Attendance Logs",
        "Security Logs",
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


def get_security_event_type(error_message: str, default_event_type: str):
    """
    Convert common face/image errors into clear security event types.
    """

    if "No face" in error_message:
        return "NO_FACE_DETECTED"

    if "Multiple" in error_message:
        return "MULTIPLE_FACES_DETECTED"

    if "No enrolled users" in error_message:
        return "NO_ENROLLED_USERS"

    return default_event_type


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
            error_message = str(error)

            with left_col:
                st.error(error_message)

            event_type = get_security_event_type(
                error_message=error_message,
                default_event_type="ENROLLMENT_ERROR",
            )

            log_security_event(
                event_type=event_type,
                message=error_message,
            )


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

                        log_security_event(
                            event_type="FAILED_VERIFICATION",
                            message="Face verification failed. The face was not recognized.",
                            face_distance=verification_result["distance"],
                        )

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

                            log_security_event(
                                event_type="DUPLICATE_ATTENDANCE",
                                message=attendance_result["message"],
                                student_id=verification_result["student_id"],
                                full_name=verification_result["full_name"],
                                face_distance=verification_result["distance"],
                            )

                except Exception as error:
                    error_message = str(error)
                    st.error(error_message)

                    event_type = get_security_event_type(
                        error_message=error_message,
                        default_event_type="VERIFICATION_ERROR",
                    )

                    log_security_event(
                        event_type=event_type,
                        message=error_message,
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
                errors="coerce",
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

                date_range = st.date_input(
                    "Filter by Date Range",
                    value=(default_start_date, default_end_date),
                    key="attendance_date_range",
                )
            else:
                date_range = None

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
            st.metric("Unique Students", filtered_df["student_id"].nunique())

        with metric_col3:
            st.metric("Attendance Days", filtered_df["attendance_date"].nunique())

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


elif menu == "Security Logs":
    require_admin_access("Security Logs")
    
    st.subheader("Security Logs")

    security_logs = get_security_logs()

    if not security_logs:
        st.info("No security logs found yet.")

    else:
        df = pd.DataFrame(security_logs)

        if "created_at" in df.columns:
            df["created_at"] = pd.to_datetime(
                df["created_at"],
                errors="coerce",
            )

            df["created_date"] = df["created_at"].dt.date

        st.subheader("Filters")

        filter_col1, filter_col2, filter_col3 = st.columns(3)

        with filter_col1:
            event_options = sorted(df["event_type"].dropna().unique().tolist())

            selected_events = st.multiselect(
                "Filter by Event Type",
                options=event_options,
                default=event_options,
            )

        with filter_col2:
            search_query = st.text_input(
                "Search Student, Name, or Message",
                placeholder="Example: S001, Mohamad, failed",
            )

        with filter_col3:
            if "created_date" in df.columns:
                available_dates = sorted(df["created_date"].dropna().unique())

                if available_dates:
                    date_range = st.date_input(
                        "Filter by Date Range",
                        value=(available_dates[0], available_dates[-1]),
                        key="security_date_range",
                    )
                else:
                    date_range = None
            else:
                date_range = None

        filtered_df = df.copy()

        if selected_events:
            filtered_df = filtered_df[
                filtered_df["event_type"].isin(selected_events)
            ]

        if search_query:
            search_query = search_query.lower().strip()

            filtered_df = filtered_df[
                filtered_df["student_id"].astype(str).str.lower().str.contains(search_query)
                | filtered_df["full_name"].astype(str).str.lower().str.contains(search_query)
                | filtered_df["message"].astype(str).str.lower().str.contains(search_query)
            ]

        if date_range and len(date_range) == 2 and "created_date" in filtered_df.columns:
            start_date, end_date = date_range

            filtered_df = filtered_df[
                (filtered_df["created_date"] >= start_date)
                & (filtered_df["created_date"] <= end_date)
            ]

        st.subheader("Summary")

        metric_col1, metric_col2, metric_col3 = st.columns(3)

        with metric_col1:
            st.metric("Total Security Events", len(filtered_df))

        with metric_col2:
            st.metric("Event Types", filtered_df["event_type"].nunique())

        with metric_col3:
            flagged_count = len(
                filtered_df[
                    filtered_df["event_type"].astype(str).str.contains(
                        "FAILED|ERROR|NO_FACE|MULTIPLE|DUPLICATE",
                        case=False,
                        regex=True,
                    )
                ]
            )

            st.metric("Flagged Events", flagged_count)

        st.subheader("Security Event Records")

        if filtered_df.empty:
            st.warning("No security logs match the selected filters.")

        else:
            st.dataframe(
                filtered_df,
                use_container_width=True,
                height=420,
            )

            csv_data = filtered_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="Download Security Logs as CSV",
                data=csv_data,
                file_name="security_logs.csv",
                mime="text/csv",
                use_container_width=True,
            )


elif menu == "Database Status":
    require_admin_access("Database Status")
    st.subheader("Database Status")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Registered Users", get_users_count())

    with col2:
        st.metric("Face Profiles", get_face_profiles_count())

    with col3:
        st.metric("Attendance Logs", get_attendance_logs_count())

    with col4:
        st.metric("Security Logs", get_security_logs_count())

    st.divider()

    st.info(
        "This page shows local system statistics. "
        "Do not upload local database files, face images, or biometric data to GitHub."
    )