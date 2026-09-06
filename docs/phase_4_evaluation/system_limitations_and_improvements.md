# System Limitations and Future Improvements

## Project

Secure Attendance System with Face Authentication

## Phase

Phase 4: Evaluation, Optimization, and Model Refinement

## Purpose

This document summarizes the current strengths, limitations, and possible future improvements of the Secure Attendance System after Phase 4 evaluation.

The detailed threshold testing results are documented in `threshold_testing_plan.md`, and the lighting and pose testing results are documented in `lighting_pose_testing_matrix.md`. This file focuses only on the system’s limitations and improvement opportunities.

---

## 1. Current System Strengths

By the end of Phase 4, the system supported the main functional requirements of the internship project.

| Feature | Status |
|---|---|
| User enrollment | Implemented |
| Face verification | Implemented |
| Attendance recording | Implemented |
| Duplicate attendance prevention | Implemented |
| Attendance dashboard | Implemented |
| Attendance CSV export | Implemented |
| Security logs | Implemented |
| Admin access control | Implemented |
| Duplicate student ID prevention | Implemented |
| Duplicate face enrollment prevention | Implemented |
| Threshold evaluation script | Implemented |
| Local privacy handling | Implemented through `.gitignore` and local-only testing |

These features show that the system is a functional local prototype for face-authenticated attendance management.

---

## 2. Current Limitations

Although the system is functional, Phase 4 evaluation showed several limitations that should be considered before real-world deployment.

| Limitation | Explanation |
|---|---|
| Image quality dependence | The system works best with clear, front-facing images. Poor lighting, blur, or overexposure may reduce reliability. |
| Pose sensitivity | Side-facing or tilted images may increase face distance or cause face detection failure. |
| Limited evaluation dataset | Testing was performed using a small local test set. A larger dataset with more users would improve evaluation reliability. |
| No advanced liveness detection | The system does not yet verify whether the face is live, so advanced anti-spoofing is not implemented. |
| Same image reuse risk | If the same enrollment image is reused during verification, the distance may become `0.0000`, which is expected but not realistic for attendance. |
| Local database only | SQLite is suitable for prototype development but is not ideal for large-scale institutional deployment. |
| No database encryption yet | Stored biometric encodings are kept locally but are not encrypted in the current prototype. |
| Basic admin access control | The system uses a simple admin password for protected pages, not a full authentication and role-management system. |

---

## 3. Limitation Details

### 3.1 Image Quality Dependence

The system performs best when the submitted image is clear, front-facing, and well-lit. Poor lighting, blur, or overexposure can increase the face distance and reduce verification reliability.

### 3.2 Pose Sensitivity

The side-pose test showed that face orientation can affect detection. When the face is turned too far from the camera, the system may fail to detect a face.

### 3.3 Limited Evaluation Dataset

The evaluation was performed using a small number of local test images. This is acceptable for a prototype, but stronger conclusions would require testing with more users, more images, and more varied conditions.

### 3.4 No Advanced Liveness Detection

The current prototype does not include strong anti-spoofing or liveness detection. It does not yet verify whether the face comes from a real live person rather than a printed image, replayed video, or another spoofing attempt.

### 3.5 Same Image Reuse

If the exact same image used during enrollment is uploaded again during verification, the face distance may become `0.0000`. This is technically expected because both encodings come from the same image, but real attendance verification should use a different image, preferably captured live.

### 3.6 No Database Encryption Yet

The system keeps biometric-related data local and excludes database files from GitHub. However, the facial encodings stored in the local SQLite database are not encrypted in the current prototype. Encryption should be added in future versions to improve biometric data protection.

---

## 4. Future Improvements

Future work can improve system reliability, security, privacy, and deployment readiness.

| Future Improvement | Purpose |
|---|---|
| Image quality validation | Detect blurry, dark, or overexposed images before verification |
| Pose validation | Detect non-frontal or tilted faces before attempting recognition |
| Liveness detection | Reduce spoofing risk from printed photos, replayed videos, or fake faces |
| Larger test dataset | Improve evaluation reliability using more users and image conditions |
| FAR / FRR analysis | Measure false acceptance and false rejection rates more formally |
| Camera-only verification mode | Reduce the risk of reused enrollment images |
| Database encryption | Encrypt stored facial encodings and local database files |
| Stronger authentication | Replace basic admin password access with full login and role-based access control |
| Deployment preparation | Prepare the system for controlled institutional use |
| Improved reporting dashboard | Add more analytics, charts, and export options |
| Backup and recovery support | Protect attendance records against accidental local data loss |

---

## 5. Privacy and Security Improvement Priorities

The most important future privacy and security improvements are:

1. Add database encryption for stored facial encodings.
2. Add stronger admin authentication and role-based access control.
3. Add liveness detection to reduce spoofing risk.
4. Add image quality checks before verification.
5. Continue excluding local databases, face images, and biometric data from GitHub.

These improvements would make the system more suitable for real-world deployment beyond the academic prototype stage.

---

## 6. Summary

The current system satisfies the main functional requirements of the internship project. It supports user enrollment, face verification, attendance recording, duplicate prevention, reporting, security logs, admin access control, and local evaluation.

The main remaining limitations are related to image quality, pose sensitivity, limited testing data, lack of advanced liveness detection, basic access control, and lack of database encryption.

Overall, the system is a functional and privacy-aware academic prototype, but future versions should improve robustness, security, biometric data protection, and real-world deployment readiness.