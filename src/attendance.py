from src.database import record_attendance_log


def mark_attendance(user_id: int, face_distance: float | None = None):
    """
    Record attendance for a verified user.

    This function uses the database layer to:
    - create/get today's attendance session
    - record the user's attendance
    - prevent duplicate check-in on the same day
    """

    if user_id is None:
        raise ValueError("User ID is required to record attendance.")

    return record_attendance_log(
        user_id=user_id,
        face_distance=face_distance,
        status="present",
    )