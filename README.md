# Secure Attendance System with Face Authentication

**Developer:** Mohamad El Saleh

**Host Institution:** International Center for AI and Cyber Security Research and Innovations (CCRI)

**Academic Affiliation:** Lebanese University Faculty of Engineering (ULFG)

---

## Current Project Status

This repository currently represents the progress of the **Secure Attendance System with Face Authentication** project up to **Phase 2**.

Phase 1 focused on literature review, system design, database planning, and prototype testing. Phase 2 extended the project into a working local MVP that supports face enrollment, face verification, attendance recording, duplicate check-in prevention, and attendance log viewing through a Streamlit dashboard.

The current implementation is developed on the `phase-2-local-streamlit` branch and includes the first functional version of the attendance workflow.

---

## Project Overview

Traditional attendance tracking methods are vulnerable to proxy attendance, credential sharing, manual errors, and administrative delays. This project aims to develop a secure attendance system that uses face authentication to verify a user's identity before recording attendance.

The system detects a face from a captured or uploaded image, generates a 128-dimensional facial encoding, compares it with stored user profiles, and records attendance after successful verification.

The current Phase 2 MVP supports:

* User registration
* Face enrollment
* Facial encoding storage
* Face verification
* Automatic attendance recording
* Duplicate check-in prevention
* Attendance log viewing
* CSV export of attendance records

---

## Repository Architecture and Navigation

```text
Secure-Attendance-System-Using-Facial-Recognition/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── database.py
│   ├── face_enrollment.py
│   ├── face_verification.py
│   └── attendance.py
│
├── docs/
│   └── PHASE_1_DOCUMENTATION.md
│
├── research_sandbox/
│   └── Phase1_Vision_and_DB_Tests.ipynb
│
└── data/
    └── Local database files ignored by Git
```

### Main Files

| File                                                | Description                                                               |
| --------------------------------------------------- | ------------------------------------------------------------------------- |
| `app.py`                                            | Main Streamlit dashboard interface                                        |
| `src/database.py`                                   | SQLite database creation and query handling                               |
| `src/face_enrollment.py`                            | User registration, image conversion, face detection, and encoding storage |
| `src/face_verification.py`                          | Face comparison and identity verification                                 |
| `src/attendance.py`                                 | Attendance recording and duplicate check-in handling                      |
| `docs/PHASE_1_DOCUMENTATION.md`                     | Phase 1 research and system design documentation                          |
| `research_sandbox/Phase1_Vision_and_DB_Tests.ipynb` | Prototype notebook for early face encoding and database testing           |

---

## Core Technology Stack

| Component              | Technology                       |
| ---------------------- | -------------------------------- |
| Programming Language   | Python                           |
| Web Interface          | Streamlit                        |
| Face Recognition       | dlib / `face_recognition`        |
| Face Representation    | 128-dimensional facial encodings |
| Image Handling         | Pillow, OpenCV headless          |
| Numerical Processing   | NumPy                            |
| Data Handling          | Pandas                           |
| Database               | SQLite                           |
| Environment Management | Conda                            |

---

## Implemented Features

### Phase 1: Research and Prototype Testing

* Literature review on facial recognition and biometric authentication.
* Study of face detection, face recognition, and attendance management techniques.
* Definition of system requirements and architecture.
* SQLite database and attendance management framework design.
* Prototype testing using Jupyter/Google Colab.
* Initial testing of face encodings and distance-based comparison.

### Phase 2: Enrollment, Verification, and Attendance MVP

* Created a local development environment using Conda and Python 3.10.
* Implemented SQLite database tables for users, facial profiles, attendance sessions, and attendance logs.
* Developed the face enrollment module.
* Added support for camera input and image upload using Streamlit.
* Converted face images into valid RGB `uint8` NumPy arrays.
* Generated and stored 128-dimensional facial encodings.
* Developed the face verification module using distance-based matching.
* Displayed face distance values after verification.
* Connected successful verification to attendance recording.
* Added duplicate check-in prevention for the same user on the same day.
* Improved the verification workflow so attendance is processed automatically after image capture or upload.
* Added an attendance logs page.
* Added CSV export for attendance records.
* Added a database status page showing system counts.

---

## System Workflow

```text
Register User
    ↓
Capture or Upload Face Image
    ↓
Detect Face
    ↓
Generate 128-D Face Encoding
    ↓
Store User and Face Encoding in SQLite
    ↓
Verify Attendance
    ↓
Compare New Face Encoding with Stored Encodings
    ↓
If Match is Successful
    ↓
Record Attendance and Prevent Duplicate Check-in
    ↓
Display Attendance Logs / Export CSV
```

---

## Streamlit Dashboard Pages

### 1. Register User

Allows the user to enter student information and enroll a face image. The system detects the face, generates a facial encoding, and stores it in the SQLite database.

### 2. Verify Attendance

Allows the user to capture or upload a new face image. The system automatically verifies the face and records attendance if the match is successful.

### 3. View Attendance Logs

Displays attendance records in a table and allows exporting the logs as a CSV file.

### 4. Database Status

Displays basic system statistics, including the number of registered users, stored facial profiles, and attendance logs.

---

## Database Design

The system uses SQLite as the local database.

| Table                 | Purpose                                                          |
| --------------------- | ---------------------------------------------------------------- |
| `users`               | Stores student ID, full name, email, role, and creation time     |
| `facial_profiles`     | Stores the face encoding linked to each user                     |
| `attendance_sessions` | Stores daily attendance session information                      |
| `attendance_logs`     | Stores attendance date, check-in time, status, and face distance |

Local database files are not uploaded to GitHub because they may contain sensitive biometric information.

---

## Face Verification Logic

The system uses distance-based face matching.

```text
If best_face_distance <= tolerance:
    User is verified
Else:
    Face is rejected
```

The current default tolerance is:

```text
0.60
```

This value is suitable for the current MVP and will be further evaluated in later phases using multiple users, lighting conditions, and camera angles.

---

## How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Mohamad-101/Secure-Attendance-System-Using-Facial-Recognition.git
cd Secure-Attendance-System-Using-Facial-Recognition
```

### 2. Create and activate Conda environment

```bash
conda create -n attendance python=3.10 -y
conda activate attendance
```

### 3. Install dependencies

```bash
conda install -c conda-forge dlib -y
python -m pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

---

## Project Development Roadmap

### Phase 1: Research, Architecture, and Prototype Testing

* [x] Review facial recognition and biometric authentication concepts.
* [x] Study face detection, face recognition, and attendance management techniques.
* [x] Define system requirements and architecture.
* [x] Set up the development environment.
* [x] Design the SQLite database and attendance framework.
* [x] Test face encoding and distance comparison in prototype notebook.
* [x] Insert demo database records for early testing.

### Phase 2: Enrollment, Verification, and Dashboard

* [x] Build user enrollment and facial profile registration module.
* [x] Move notebook logic into reusable Python modules.
* [x] Implement SQLite database layer.
* [x] Implement face verification using stored encodings.
* [x] Implement attendance recording after successful verification.
* [x] Add duplicate check-in prevention.
* [x] Build Streamlit dashboard interface.
* [x] Add attendance logs page.
* [x] Add CSV export.

### Phase 3: Security, Reporting, and Evaluation

* [ ] Add basic anti-spoofing or image quality checks.
* [ ] Add failed verification logging.
* [ ] Test the system with multiple users.
* [ ] Evaluate recognition under different lighting and pose conditions.
* [ ] Improve dashboard user experience.
* [ ] Add access control and security mechanisms.
* [ ] Improve documentation and reporting.

---

## Privacy and Data Handling

Facial data is sensitive biometric information. The project follows basic privacy precautions during development:

* Local database files are ignored by Git.
* Test face images are not uploaded to the repository.
* Biometric files and local data folders are excluded using `.gitignore`.
* Screenshots used in reports or presentations should be blurred or cropped to hide faces.
* Facial encodings should be treated as sensitive data.

Recommended future improvements include database encryption, admin authentication, access control, and stronger privacy protection for biometric data.

---

## Current Limitations

* The current version uses captured/uploaded images rather than continuous live video.
* Anti-spoofing and liveness detection are not fully implemented yet.
* Testing has been limited to a small number of users.
* SQLite is suitable for local development, but a cloud database may be needed for deployment.
* Dashboard access is not yet protected by authentication.
* Face recognition threshold still needs more evaluation.

---

## Next Steps

The next phase will focus on improving security and reliability:

* Add basic anti-spoofing or image quality validation.
* Add failed or suspicious attempt logging.
* Test with multiple users and different image conditions.
* Improve recognition threshold evaluation.
* Improve Streamlit interface design.
* Add access control for dashboard pages.
* Prepare more complete technical documentation and project report.

---

## Notes

This repository is part of the CCRI International Summer Internship project. The current branch contains the Phase 2 MVP implementation. Future phases will focus on security improvements, testing, reporting, optimization, and final deployment.
