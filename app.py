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
        .stApp {
            background: linear-gradient(180deg, #f7f9fc 0%, #ffffff 45%);
        }

        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 2rem;
            max-width: 1250px;
        }

        h1 {
            font-size: 2.5rem !important;
            font-weight: 800 !important;
            letter-spacing: -0.04em;
            margin-bottom: 0.15rem !important;
            color: #1f2937;
        }

        h2 {
            font-size: 1.65rem !important;
            font-weight: 750 !important;
            color: #111827;
        }

        h3 {
            font-size: 1.15rem !important;
            font-weight: 700 !important;
            color: #1f2937;
        }

        .app-subtitle {
            color: #6b7280;
            font-size: 1rem;
            margin-bottom: 1.3rem;
        }

        .hero-card {
            background: linear-gradient(135deg, #111827 0%, #1f2937 55%, #374151 100%);
            color: white;
            border-radius: 20px;
            padding: 1.3rem 1.5rem;
            margin-bottom: 1.2rem;
            box-shadow: 0 12px 30px rgba(17, 24, 39, 0.12);
        }

        .hero-card h2 {
            color: white !important;
            margin-bottom: 0.4rem !important;
        }

        .hero-card p {
            color: #d1d5db;
            margin-bottom: 0;
            line-height: 1.6;
        }

        .info-card {
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            padding: 1rem 1.1rem;
            box-shadow: 0 4px 18px rgba(15, 23, 42, 0.05);
            margin-bottom: 0.8rem;
        }

        .info-card h3 {
            margin-top: 0 !important;
            margin-bottom: 0.35rem !important;
        }

        .info-card p {
            color: #4b5563;
            margin-bottom: 0;
            line-height: 1.55;
        }

        .section-note {
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            color: #1e3a8a;
            border-radius: 14px;
            padding: 0.85rem 1rem;
            margin-bottom: 1rem;
            line-height: 1.55;
        }

        .privacy-note {
            background: #ecfdf5;
            border: 1px solid #a7f3d0;
            color: #065f46;
            border-radius: 14px;
            padding: 0.85rem 1rem;
            margin-bottom: 1rem;
            line-height: 1.55;
        }

        .warning-note {
            background: #fffbeb;
            border: 1px solid #fde68a;
            color: #92400e;
            border-radius: 14px;
            padding: 0.85rem 1rem;
            margin-bottom: 1rem;
            line-height: 1.55;
        }

        .small-label {
            font-size: 0.78rem;
            font-weight: 700;
            color: #6b7280;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.25rem;
        }

        .status-pill {
            display: inline-block;
            background: #dcfce7;
            color: #166534;
            font-weight: 700;
            font-size: 0.78rem;
            padding: 0.25rem 0.7rem;
            border-radius: 999px;
            border: 1px solid #bbf7d0;
            margin-bottom: 0.5rem;
        }

        div[data-testid="stVerticalBlock"] {
            gap: 0.65rem;
        }

        section[data-testid="stSidebar"] {
            width: 280px !important;
            background: #f8fafc;
            border-right: 1px solid #e5e7eb;
        }

        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: #111827 !important;
        }

        .sidebar-title {
            font-size: 1.05rem;
            font-weight: 800;
            color: #111827;
            margin-bottom: 0.2rem;
        }

        .sidebar-caption {
            color: #6b7280;
            font-size: 0.85rem;
            line-height: 1.45;
            margin-bottom: 1rem;
        }

        .stButton > button {
            border-radius: 12px;
            font-weight: 700;
            border: 1px solid #d1d5db;
        }

        .stDownloadButton > button {
            border-radius: 12px;
            font-weight: 700;
        }

        div[data-testid="stMetric"] {
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            padding: 0.8rem 1rem;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
        }

        .dataframe {
            border-radius: 14px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


init_db()


def render_main_header():
    st.title("Secure Attendance System")
    st.markdown(
        """
        <div class="app-subtitle">
            Face Enrollment, Identity Verification, Attendance Logging, Reporting, and Security Monitoring
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_page_header(title: str, description: str):
    st.header(title)
    st.markdown(
        f"""
        <div class="section-note">
            {description}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_info_card(title: str, body: str):
    st.markdown(
        f"""
        <div class="info-card">
            <h3>{title}</h3>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_privacy_note():
    st.markdown(
        """
        <div class="privacy-note">
            <strong>Privacy reminder:</strong> Face images, biometric encodings, and local database files
            should remain private and should not be uploaded to GitHub.
        </div>
        """,
        unsafe_allow_html=True,
    )


render_main_header()


st.sidebar.markdown(
    """
    <div class="sidebar-title">Secure Attendance</div>
    <div class="sidebar-caption">
        Final demo interface for enrollment, verification, attendance reports, and security monitoring.
    </div>
    """,
    unsafe_allow_html=True,
)

menu = st.sidebar.radio(
    "Navigation",
    [
        "System Overview",
        "Register User",
        "Verify Attendance",
        "View Attendance Logs",
        "Security Logs",
        "Database Status",
    ],
)

st.sidebar.divider()
st.sidebar.markdown("### System Snapshot")
st.sidebar.metric("Users", get_users_count())
st.sidebar.metric("Attendance Logs", get_attendance_logs_count())
st.sidebar.metric("Security Events", get_security_logs_count())
st.sidebar.caption("Sensitive pages require admin access.")


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


if menu == "System Overview":
    st.markdown(
        """
        <div class="hero-card">
            <span class="status-pill">Final Demo Preparation</span>
            <h2>System Overview</h2>
            <p>
                This dashboard summarizes the current Secure Attendance System and provides
                a clean entry point for final demonstration, testing, and assessment.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

    with metric_col1:
        st.metric("Registered Users", get_users_count())

    with metric_col2:
        st.metric("Face Profiles", get_face_profiles_count())

    with metric_col3:
        st.metric("Attendance Logs", get_attendance_logs_count())

    with metric_col4:
        st.metric("Security Logs", get_security_logs_count())

    st.subheader("Main Workflow")

    workflow_col1, workflow_col2, workflow_col3 = st.columns(3)

    with workflow_col1:
        render_info_card(
            "1. Enrollment",
            "Register a user with student information and one clear face image. "
            "The system stores the generated face encoding locally.",
        )

    with workflow_col2:
        render_info_card(
            "2. Verification",
            "Verify a submitted face image against enrolled facial profiles using "
            "face-distance comparison.",
        )

    with workflow_col3:
        render_info_card(
            "3. Attendance",
            "When verification succeeds, attendance is recorded automatically while "
            "duplicate attendance is prevented.",
        )

    st.subheader("Final Demo Guide")

    demo_col1, demo_col2 = st.columns([1.1, 1])

    with demo_col1:
        st.markdown(
            """
            1. Open **Register User** and enroll a test user.
            2. Open **Verify Attendance** and verify the enrolled face.
            3. Repeat the verification to show duplicate attendance prevention.
            4. Open **View Attendance Logs** to show reporting and CSV export.
            5. Open **Security Logs** using the admin password.
            6. Open **Database Status** to show local system statistics.
            """
        )

    with demo_col2:
        render_info_card(
            "Completed Modules",
            "Enrollment, verification, attendance logging, reporting, security monitoring, "
            "admin access control, duplicate prevention, and threshold evaluation documentation.",
        )

    render_privacy_note()

    st.markdown(
        """
        <div class="warning-note">
            <strong>Current limitation:</strong> The system works best with clear, front-facing images.
            Advanced liveness detection and anti-spoofing checks are planned as future improvements.
        </div>
        """,
        unsafe_allow_html=True,
    )


elif menu == "Register User":
    render_page_header(
        "Register User",
        "Enroll a new user by entering student information and providing one clear face image.",
    )

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
        render_privacy_note()

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

                result_col1, result_col2 = st.columns(2)

                with result_col1:
                    st.write(f"**User ID:** {result['user_id']}")
                    st.write(f"**Student ID:** {result['student_id']}")
                    st.write(f"**Role:** {result['role']}")

                with result_col2:
                    st.write(f"**Full Name:** {result['full_name']}")
                    st.write(f"**Email:** {result['email']}")

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
    render_page_header(
        "Verify Attendance",
        "Verify a face image against enrolled profiles and record attendance automatically.",
    )

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

        st.caption(
            "Lower tolerance is stricter. The default value of 0.60 is used for normal verification."
        )

        result_area = st.container()

    with right_col:
        st.subheader("Face Image")
        st.caption("Use a clear, front-facing image.")
        image_file = get_face_input("verify")
        render_privacy_note()

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
    render_page_header(
        "Attendance Logs",
        "Review attendance records, apply filters, and export filtered results as CSV.",
    )

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

    render_page_header(
        "Security Logs",
        "Review failed verification, duplicate attendance, enrollment errors, and admin access events.",
    )

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
                        "FAILED|ERROR|NO_FACE|MULTIPLE|DUPLICATE|ACCESS_DENIED",
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

    render_page_header(
        "Database Status",
        "View local system statistics for the current Streamlit and SQLite setup.",
    )

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