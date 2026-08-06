import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import face_recognition
import numpy as np

from src.database import init_db, get_all_face_profiles
from src.face_enrollment import get_single_face_encoding


THRESHOLDS = [0.45, 0.50, 0.55, 0.60, 0.65]


def evaluate_image(image_path: str):
    init_db()

    image_path = Path(image_path)

    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    profiles = get_all_face_profiles()

    if not profiles:
        raise ValueError("No enrolled face profiles found in the database.")

    with image_path.open("rb") as image_file:
        test_encoding = get_single_face_encoding(image_file)

    known_encodings = []

    for profile in profiles:
        if "encoding" in profile:
            known_encodings.append(profile["encoding"])
        elif "face_encoding" in profile:
            known_encodings.append(profile["face_encoding"])
        else:
            raise ValueError(f"No encoding found in profile keys: {list(profile.keys())}")

    distances = face_recognition.face_distance(known_encodings, test_encoding)

    best_index = int(np.argmin(distances))
    best_distance = float(distances[best_index])
    best_profile = profiles[best_index]

    print()
    print("Phase 4 Threshold Evaluation")
    print("-" * 45)
    print(f"Test image: {image_path}")
    print(f"Best matched student ID: {best_profile['student_id']}")
    print(f"Best matched full name: {best_profile['full_name']}")
    print(f"Best face distance: {best_distance:.4f}")
    print("-" * 45)

    for threshold in THRESHOLDS:
        result = "ACCEPTED" if best_distance <= threshold else "REJECTED"
        print(f"Tolerance {threshold:.2f}: {result}")

    print("-" * 45)
    print("Note: Distance 0.0000 can happen when the exact enrollment image is reused.")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Evaluate one face image against enrolled users using multiple tolerance values."
    )

    parser.add_argument(
        "image_path",
        help="Path to the local face image to evaluate.",
    )

    args = parser.parse_args()
    evaluate_image(args.image_path)