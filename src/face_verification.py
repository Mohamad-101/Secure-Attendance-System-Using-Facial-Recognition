import numpy as np
import face_recognition

from src.database import get_all_face_profiles
from src.face_enrollment import get_single_face_encoding


def verify_face(image_file, tolerance: float = 0.6):
    """
    Verify a face image against stored facial profiles.

    Returns:
        dict with match status, user information, and face distance.
    """

    if image_file is None:
        raise ValueError("Face image is required.")

    if tolerance <= 0:
        raise ValueError("Tolerance must be greater than 0.")

    input_encoding = get_single_face_encoding(image_file)

    profiles = get_all_face_profiles()

    if not profiles:
        raise ValueError("No enrolled users found. Please register a user first.")

    known_encodings = [profile["encoding"] for profile in profiles]

    distances = face_recognition.face_distance(
        known_encodings,
        input_encoding
    )

    best_match_index = int(np.argmin(distances))
    best_distance = float(distances[best_match_index])
    best_profile = profiles[best_match_index]

    if best_distance <= tolerance:
        return {
            "matched": True,
            "user_id": best_profile["user_id"],
            "student_id": best_profile["student_id"],
            "full_name": best_profile["full_name"],
            "email": best_profile["email"],
            "role": best_profile["role"],
            "distance": best_distance,
            "message": "Face verified successfully.",
        }

    return {
        "matched": False,
        "distance": best_distance,
        "message": "Face not recognized.",
    }