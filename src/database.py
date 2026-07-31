from pathlib import Path
import sqlite3
import io
from datetime import date, datetime

import numpy as np


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "attendance.db"


def get_connection():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    return conn


def encoding_to_blob(encoding: np.ndarray) -> bytes:
    buffer = io.BytesIO()
    np.save(buffer, encoding)
    return buffer.getvalue()


def blob_to_encoding(blob: bytes) -> np.ndarray:
    buffer = io.BytesIO(blob)
    buffer.seek(0)
    return np.load(buffer, allow_pickle=False)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE NOT NULL,
            full_name TEXT NOT NULL,
            email TEXT UNIQUE,
            role TEXT DEFAULT 'student',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS facial_profiles (
            profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE NOT NULL,
            face_encoding BLOB NOT NULL,
            enrollment_date TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS attendance_sessions (
            session_id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_name TEXT NOT NULL,
            session_date TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(session_name, session_date)
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS attendance_logs (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            session_id INTEGER,
            attendance_date TEXT NOT NULL,
            check_in_time TEXT NOT NULL,
            status TEXT DEFAULT 'present',
            face_distance REAL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, attendance_date),
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
            FOREIGN KEY (session_id) REFERENCES attendance_sessions(session_id) ON DELETE SET NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS security_logs (
            security_log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_type TEXT NOT NULL,
            message TEXT NOT NULL,
            student_id TEXT,
            full_name TEXT,
            face_distance REAL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    conn.close()


def create_or_update_user(
    student_id: str,
    full_name: str,
    email: str | None = None,
    role: str = "student",
) -> int:
    conn = get_connection()
    cursor = conn.cursor()

    student_id = student_id.strip()
    full_name = full_name.strip()
    email = email.strip() if email else None
    role = role.strip() if role else "student"

    cursor.execute(
        """
        INSERT INTO users (student_id, full_name, email, role)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(student_id)
        DO UPDATE SET
            full_name = excluded.full_name,
            email = excluded.email,
            role = excluded.role
        """,
        (student_id, full_name, email, role),
    )

    cursor.execute(
        """
        SELECT user_id
        FROM users
        WHERE student_id = ?
        """,
        (student_id,),
    )

    user = cursor.fetchone()

    conn.commit()
    conn.close()

    return user["user_id"]


def save_face_profile(user_id: int, encoding: np.ndarray):
    conn = get_connection()
    cursor = conn.cursor()

    encoding_blob = encoding_to_blob(encoding)

    cursor.execute(
        """
        INSERT INTO facial_profiles (user_id, face_encoding)
        VALUES (?, ?)
        ON CONFLICT(user_id)
        DO UPDATE SET
            face_encoding = excluded.face_encoding,
            enrollment_date = CURRENT_TIMESTAMP
        """,
        (user_id, encoding_blob),
    )

    conn.commit()
    conn.close()


def get_all_face_profiles():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            users.user_id,
            users.student_id,
            users.full_name,
            users.email,
            users.role,
            facial_profiles.face_encoding
        FROM facial_profiles
        JOIN users ON facial_profiles.user_id = users.user_id
        """
    )

    rows = cursor.fetchall()
    conn.close()

    profiles = []

    for row in rows:
        profiles.append(
            {
                "user_id": row["user_id"],
                "student_id": row["student_id"],
                "full_name": row["full_name"],
                "email": row["email"],
                "role": row["role"],
                "encoding": blob_to_encoding(row["face_encoding"]),
            }
        )

    return profiles


def get_or_create_today_session(session_name: str = "Daily Attendance") -> int:
    today = date.today().isoformat()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO attendance_sessions (session_name, session_date)
        VALUES (?, ?)
        """,
        (session_name, today),
    )

    cursor.execute(
        """
        SELECT session_id
        FROM attendance_sessions
        WHERE session_name = ? AND session_date = ?
        """,
        (session_name, today),
    )

    session = cursor.fetchone()

    conn.commit()
    conn.close()

    return session["session_id"]


def record_attendance_log(
    user_id: int,
    face_distance: float | None = None,
    status: str = "present",
):
    today = date.today().isoformat()
    now = datetime.now().strftime("%H:%M:%S")
    session_id = get_or_create_today_session()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT log_id, check_in_time
        FROM attendance_logs
        WHERE user_id = ? AND attendance_date = ?
        """,
        (user_id, today),
    )

    existing_log = cursor.fetchone()

    if existing_log:
        conn.close()

        return {
            "recorded": False,
            "message": f"Attendance already recorded today at {existing_log['check_in_time']}.",
        }

    cursor.execute(
        """
        INSERT INTO attendance_logs (
            user_id,
            session_id,
            attendance_date,
            check_in_time,
            status,
            face_distance
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (user_id, session_id, today, now, status, face_distance),
    )

    conn.commit()
    conn.close()

    return {
        "recorded": True,
        "message": f"Attendance recorded successfully at {now}.",
    }


def get_attendance_logs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            attendance_logs.log_id,
            users.student_id,
            users.full_name,
            users.email,
            users.role,
            attendance_sessions.session_name,
            attendance_logs.attendance_date,
            attendance_logs.check_in_time,
            attendance_logs.status,
            attendance_logs.face_distance
        FROM attendance_logs
        JOIN users ON attendance_logs.user_id = users.user_id
        LEFT JOIN attendance_sessions
            ON attendance_logs.session_id = attendance_sessions.session_id
        ORDER BY attendance_logs.attendance_date DESC, attendance_logs.check_in_time DESC
        """
    )

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


def get_users_count() -> int:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) AS count FROM users")
    result = cursor.fetchone()

    conn.close()

    return result["count"]


def get_face_profiles_count() -> int:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) AS count FROM facial_profiles")
    result = cursor.fetchone()

    conn.close()

    return result["count"]


def get_attendance_logs_count() -> int:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) AS count FROM attendance_logs")
    result = cursor.fetchone()

    conn.close()

    return result["count"]


def log_security_event(
    event_type: str,
    message: str,
    student_id: str | None = None,
    full_name: str | None = None,
    face_distance: float | None = None,
):
    """
    Save a failed, duplicate, or suspicious verification event.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO security_logs (
            event_type,
            message,
            student_id,
            full_name,
            face_distance
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            event_type,
            message,
            student_id,
            full_name,
            face_distance,
        ),
    )

    conn.commit()
    conn.close()


def get_security_logs():
    """
    Return all security logs ordered from newest to oldest.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            security_log_id,
            event_type,
            message,
            student_id,
            full_name,
            face_distance,
            created_at
        FROM security_logs
        ORDER BY created_at DESC
        """
    )

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


def get_security_logs_count() -> int:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) AS count FROM security_logs")
    result = cursor.fetchone()

    conn.close()

    return result["count"]