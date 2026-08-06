import numpy as np
from PIL import Image
import face_recognition

from src.database import (
    create_or_update_user,
    save_face_profile,
    get_all_face_profiles,
    get_user_by_student_id,
)


def image_file_to_rgb_array(image_file) -> np.ndarray:
    """
    Convert a Streamlit camera/upload image into a valid 8-bit RGB NumPy array.
    Required format for dlib/face_recognition:
    - dtype: uint8
    - shape: height, width, 3
    - color: RGB
    """
    if image_file is None:
        raise ValueError("No image provided.")

    try:
        image_file.seek(0)
    except Exception:
        pass

    image = Image.open(image_file)

    # Remove transparency / palette / grayscale problems
    image = image.convert("RGB")

    image_array = np.array(image, dtype=np.uint8)

    if image_array.ndim != 3:
        raise ValueError(f"Invalid image dimensions: {image_array.shape}")

    if image_array.shape[2] != 3:
        raise ValueError(f"Invalid image channels: {image_array.shape}")

    image_array = np.ascontiguousarray(image_array)

    return image_array


def get_single_face_encoding(image_file) -> np.ndarray:
    """
    Detect exactly one face and return its 128-dimensional face encoding.
    """
    image_array = image_file_to_rgb_array(image_file)


    face_locations = face_recognition.face_locations(
        image_array,
        model="hog"
    )

    if len(face_locations) == 0:
        raise ValueError("No face detected. Please use a clearer face image.")

    if len(face_locations) > 1:
        raise ValueError("Multiple faces detected. Please use an image with only one face.")

    encodings = face_recognition.face_encodings(
        image_array,
        known_face_locations=face_locations
    )

    if len(encodings) == 0:
        raise ValueError("Face detected, but encoding could not be generated. Try another image.")

    return encodings[0]


DUPLICATE_FACE_TOLERANCE = 0.50


def check_duplicate_face(new_encoding, tolerance=DUPLICATE_FACE_TOLERANCE):
    """
    Compares a new face encoding with all stored face encodings.
    Returns the matched profile if the face is already enrolled.
    """

    profiles = get_all_face_profiles()

    if not profiles:
        return None

    known_encodings = []

    for profile in profiles:
        if "face_encoding" in profile:
            known_encodings.append(profile["face_encoding"])
        elif "encoding" in profile:
            known_encodings.append(profile["encoding"])
        else:
            raise ValueError(
                f"Face encoding not found in stored profile. Available keys: {list(profile.keys())}"
            )

    distances = face_recognition.face_distance(known_encodings, new_encoding)

    best_index = int(np.argmin(distances))
    best_distance = float(distances[best_index])

    if best_distance <= tolerance:
        duplicate_profile = dict(profiles[best_index])
        duplicate_profile["face_distance"] = best_distance
        return duplicate_profile

    return None


def enroll_user(student_id, full_name, email, role, image_file):
    student_id = student_id.strip()
    full_name = full_name.strip()
    email = email.strip() if email else None
    role = role.strip() if role else "student"

    if not student_id:
        raise ValueError("Student ID is required.")

    if not full_name:
        raise ValueError("Full name is required.")

    if image_file is None:
        raise ValueError("A face image is required for enrollment.")

    existing_user = get_user_by_student_id(student_id)

    if existing_user:
        raise ValueError(
            f"Student ID {student_id} is already enrolled for "
            f"{existing_user['full_name']}."
        )

    face_encoding = get_single_face_encoding(image_file)

    duplicate_face = check_duplicate_face(face_encoding)

    if duplicate_face:
        raise ValueError(
            f"This face is already enrolled as {duplicate_face['full_name']} "
            f"with Student ID {duplicate_face['student_id']}. "
            f"Face distance: {duplicate_face['face_distance']:.4f}"
        )

    user_id = create_or_update_user(
        student_id=student_id,
        full_name=full_name,
        email=email,
        role=role,
    )

    save_face_profile(user_id, face_encoding)

    return {
        "user_id": user_id,
        "student_id": student_id,
        "full_name": full_name,
        "email": email,
        "role": role,
        "message": "User enrolled successfully.",
    }