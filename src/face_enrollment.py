import numpy as np
from PIL import Image
import face_recognition

from src.database import create_or_update_user, save_face_profile


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

    print("DEBUG image:", image_array.shape, image_array.dtype)

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


def enroll_user(
    student_id: str,
    full_name: str,
    email: str | None,
    role: str,
    image_file,
):
    """
    Register or update a user and save their face encoding.
    """

    if not student_id or not student_id.strip():
        raise ValueError("Student ID is required.")
    

    if not full_name or not full_name.strip():
        raise ValueError("Full name is required.")

    if image_file is None:
        raise ValueError("Face image is required.")

    encoding = get_single_face_encoding(image_file)

    user_id = create_or_update_user(
        student_id=student_id,
        full_name=full_name,
        email=email,
        role=role,
    )

    save_face_profile(
        user_id=user_id,
        encoding=encoding,
    )

    return {
        "user_id": user_id,
        "student_id": student_id.strip(),
        "full_name": full_name.strip(),
        "email": email.strip() if email else None,
        "role": role.strip() if role else "student",
    }