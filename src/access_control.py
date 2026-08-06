import os
import streamlit as st

from src.database import log_security_event


DEFAULT_ADMIN_PASSWORD = "admin123"


def get_admin_password() -> str:
    return os.getenv("ADMIN_PASSWORD", DEFAULT_ADMIN_PASSWORD)


def require_admin_access(page_name: str) -> None:
    """
    Stops the page unless the correct admin password is entered.
    """

    auth_key = f"admin_authenticated_{page_name}"

    if st.session_state.get(auth_key):
        return

    st.subheader("Admin Access Required")

    st.info(
        f"The {page_name} page contains sensitive monitoring information "
        "and requires admin access."
    )

    password = st.text_input(
        "Enter admin password",
        type="password",
        key=f"{page_name}_admin_password",
    )

    if not password:
        st.warning(
            f"You must enter the correct admin password to access the {page_name} page."
        )
        st.stop()

    if password != get_admin_password():
        st.error("Invalid admin password.")

        log_security_event(
            event_type="ACCESS_DENIED",
            message=f"Invalid admin password attempt for {page_name}.",
        )

        st.stop()

    st.session_state[auth_key] = True
    st.success("Admin access granted.")