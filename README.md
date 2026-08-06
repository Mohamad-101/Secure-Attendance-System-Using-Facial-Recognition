# Secure Attendance System with Face Authentication

**Developer:** Mohamad El Saleh  
**Host Institution:** International Center for AI and Cyber Security Research and Innovations (CCRI)  
**Academic Affiliation:** Lebanese University Faculty of Engineering (ULFG)  
**Project Type:** CCRI Summer Research Internship Project  
**Field:** Artificial Intelligence, Computer Vision, Biometric Authentication, Cybersecurity, Software Engineering  

---

## Project Overview

The **Secure Attendance System with Face Authentication** is a research-internship project that aims to improve attendance management using AI-based face authentication.

Traditional attendance methods such as manual sheets, RFID cards, passwords, or shared credentials can be affected by proxy attendance, identity misuse, manual errors, and administrative delays. This project addresses these issues by verifying a user's identity using facial recognition before recording attendance.

The system allows a user to register with a face image, stores a numerical facial encoding in a local SQLite database, verifies future attendance attempts by comparing face encodings, records attendance after successful verification, and monitors failed or suspicious attempts through security logs.

---

## Current Project Status

The project has completed the main **Phase 2 MVP** and is currently finalizing **Phase 3**, which focuses on reporting, security mechanisms, access control, internal testing, debugging, and documentation.

Implemented features include:

- Student registration and face enrollment
- Face detection and facial encoding generation
- Face verification using stored encodings
- Attendance recording after successful verification
- Duplicate attendance prevention
- Attendance logs dashboard
- Attendance filtering and CSV export
- Security event logging
- Security Logs dashboard
- Admin access control for sensitive pages
- Duplicate student ID prevention
- Duplicate face enrollment prevention
- Phase 3 testing documentation

---

## Research Internship Alignment

This project follows the CCRI internship timeline and expected outcomes.

### Completed Internship Phases

| Phase | Timeline | Status | Main Work |
|---|---:|---|---|
| Phase 1 | June 6 – June 20 | Completed | Literature review, system requirements, architecture, environment setup, database design, prototype testing |
| Phase 2 | June 21 – July 10 | Completed | Face enrollment, recognition, attendance recording, verification workflow, Streamlit dashboard |
| Phase 3 | July 11 – July 31 | Finalizing | Reporting, analytics, security logging, access control, internal testing, debugging |

### Upcoming Internship Phases

| Phase | Timeline | Planned Work |
|---|---:|---|
| Phase 4 | August 1 – August 15 | Performance optimization, lighting and pose evaluation, UI enhancement, documentation preparation |
| Phase 5 | August 16 – August 31 | Final deployment, demonstration, source code submission, project report, presentation, final evaluation |

---

## Main Objectives

The main objectives of the project are:

- Develop an AI-powered attendance management system.
- Provide secure user registration and facial profile enrollment.
- Verify attendance using face authentication.
- Reduce proxy attendance and identity misuse.
- Record attendance automatically after successful verification.
- Provide a dashboard for attendance monitoring and management.
- Generate attendance reports and analytics.
- Add security mechanisms such as access control and suspicious event logging.
- Document and test the system professionally for research-internship evaluation.

---

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| User Interface | Streamlit |
| Face Recognition | `face_recognition` library / dlib pretrained model |
| Face Representation | 128-dimensional facial encodings |
| Image Processing | Pillow, OpenCV headless |
| Data Processing | NumPy, Pandas |
| Database | SQLite |
| Environment Management | Conda |
| Documentation | Markdown, weekly reports, technical articles, presentation slides |

> Note: The current implementation uses a pretrained face-recognition model through the `face_recognition` and dlib ecosystem. It does not train a custom deep learning model from scratch.

---

## Repository Structure

```text
Secure-Attendance-System-Using-Facial-Recognition/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── database.py
│   ├── face_enrollment.py
│   ├── face_verification.py
│   ├── attendance.py
│   └── access_control.py
│
├── docs/
│   ├── PHASE_1_DOCUMENTATION.md
│   └── phase_3_security_reporting/
│       ├── phase_3_summary.md
│       └── testing_matrix.md
│
├── research_sandbox/
│   └── Phase1_Vision_and_DB_Tests.ipynb
│
└── data/
    └── attendance.db
```

> The `data/` folder is used locally only. Database files and biometric data should not be uploaded to GitHub.

---

## Main Files

| File | Description |
|---|---|
| `app.py` | Main Streamlit dashboard application |
| `src/database.py` | SQLite database setup, query functions, attendance logs, and security logs |
| `src/face_enrollment.py` | User registration, image conversion, face detection, encoding generation, and duplicate enrollment prevention |
| `src/face_verification.py` | Face matching and identity verification |
| `src/attendance.py` | Attendance recording and duplicate check-in prevention |
| `src/access_control.py` | Admin access control for sensitive dashboard pages |
| `docs/PHASE_1_DOCUMENTATION.md` | Phase 1 research and design documentation |
| `docs/phase_3_security_reporting/phase_3_summary.md` | Summary of Phase 3 reporting, security, and testing work |
| `docs/phase_3_security_reporting/testing_matrix.md` | Internal testing checklist for Phase 3 |
| `research_sandbox/Phase1_Vision_and_DB_Tests.ipynb` | Early notebook prototype for face encoding and database testing |

---

## Implemented Features

### Phase 1: Research, Architecture, and Prototype Testing

- Reviewed facial recognition and biometric authentication concepts.
- Studied face detection, face recognition, and attendance management techniques.
- Defined the initial system requirements and architecture.
- Designed the SQLite database and attendance management framework.
- Tested face encoding and distance-based comparison in a prototype notebook.
- Prepared the foundation for modular Python implementation.

### Phase 2: Enrollment, Verification, and Attendance MVP

- Created a local Conda development environment using Python 3.10.
- Implemented SQLite tables for users, facial profiles, attendance sessions, and attendance logs.
- Built the face enrollment module.
- Added Streamlit camera input and image upload support.
- Converted uploaded or captured images into RGB `uint8` NumPy arrays.
- Generated and stored 128-dimensional facial encodings.
- Implemented face verification using distance-based matching.
- Displayed face distance values after verification.
- Connected successful verification to attendance recording.
- Added duplicate attendance prevention for the same user on the same day.
- Added attendance logs viewing.
- Added CSV export for attendance records.
- Added database status monitoring.

### Phase 3: Reporting, Security Logging, Access Control, and Internal Testing

- Improved attendance reporting and analytics.
- Added filtering by student ID, name, date range, and status.
- Added filtered CSV export for attendance logs.
- Added a `security_logs` database table.
- Implemented security logging functions.
- Logged failed face verification attempts.
- Logged duplicate attendance attempts.
- Logged no-face, multiple-face, no-enrolled-user, and verification error cases.
- Added a dedicated Security Logs dashboard page.
- Added security log filtering by event type, search text, and date range.
- Added CSV export for security logs.
- Added admin access control for sensitive pages.
- Protected Security Logs and Database Status pages.
- Logged wrong admin password attempts as `ACCESS_DENIED`.
- Added duplicate student ID prevention during enrollment.
- Added duplicate face enrollment prevention using face-distance comparison.
- Created Phase 3 testing documentation.

---

## System Workflow

```text
Register User
    ↓
Capture or Upload Face Image
    ↓
Detect Face
    ↓
Generate 128-Dimensional Face Encoding
    ↓
Check for Duplicate Student ID or Duplicate Face
    ↓
Store User and Face Encoding in SQLite
    ↓
Verify Attendance
    ↓
Compare New Face Encoding with Stored Encodings
    ↓
If Match is Successful
    ↓
Record Attendance
    ↓
Prevent Duplicate Check-in on the Same Day
    ↓
Display Attendance Logs and Security Logs
```

---

## Dashboard Pages

The Streamlit dashboard includes the following pages:

### 1. Register User

Used to register a student and enroll a face image. The system detects the face, generates a facial encoding, checks for duplicate student ID or duplicate face enrollment, and stores the profile in the database.

### 2. Verify Attendance

Used to verify a captured or uploaded face image. If the face matches an enrolled profile within the selected tolerance, attendance is recorded automatically.

### 3. View Attendance Logs

Used to view attendance records, search by student ID or name, filter by date range or status, view summary metrics, and export attendance records as a CSV file.

### 4. Security Logs

Used to monitor failed, duplicate, and suspicious verification events. This page is protected using admin access control.

### 5. Database Status

Used to view system statistics such as registered users, stored facial profiles, attendance logs, and security logs. This page is protected using admin access control.

---

## Database Design

The system uses SQLite as a local database.

| Table | Purpose |
|---|---|
| `users` | Stores student ID, full name, email, role, and creation time |
| `facial_profiles` | Stores the facial encoding linked to each user |
| `attendance_sessions` | Stores attendance session information |
| `attendance_logs` | Stores attendance date, check-in time, status, and face distance |
| `security_logs` | Stores failed, duplicate, suspicious, and access-denied events |

Local database files are excluded from GitHub because they may contain sensitive biometric or identity-related information.

---

## Face Verification Logic

The system uses distance-based face matching.

```text
If best_face_distance <= tolerance:
    User is verified
Else:
    Face is rejected
```

The default verification tolerance is:

```text
0.60
```

A lower distance means the submitted face is more similar to a stored face encoding. The threshold will be evaluated further during the optimization and testing phases.

---

## Duplicate Enrollment Prevention

The enrollment workflow includes validation to improve data integrity and reduce misuse.

The system blocks:

- Registering the same student ID more than once
- Registering the same face using a different student ID

The duplicate-face check compares the new face encoding with existing stored encodings before saving the new user profile.

The duplicate enrollment tolerance is stricter than the attendance verification tolerance:

```text
Attendance verification tolerance: 0.60
Duplicate face enrollment tolerance: 0.50
```

---

## Security Logs

The system includes a Security Logs module to record failed, duplicate, and suspicious events.

The security logging system can record:

- Failed face verification attempts
- Duplicate attendance attempts
- No face detected in the submitted image
- Multiple faces detected in one image
- No enrolled users available for verification
- General verification or enrollment errors
- Wrong admin password attempts

Each security log can include:

- Event type
- Message
- Student ID, when available
- Full name, when available
- Face distance, when available
- Timestamp

The Security Logs dashboard allows the admin to:

- View all security events
- Filter by event type
- Search by student ID, name, or message
- Filter by date range
- View summary metrics
- Export filtered security logs as a CSV file

---

## Access Control

Basic admin access control was added to protect sensitive dashboard pages.

Protected pages include:

- Security Logs
- Database Status

If a user tries to access a protected page without the correct admin password, access is blocked. Wrong password attempts are recorded as `ACCESS_DENIED` events in the Security Logs.

For development and demonstration, the system uses a simple admin password mechanism. In a production system, this should be replaced with stronger authentication, session management, and role-based access control.

---

## Privacy and Data Handling

Facial data is sensitive biometric information. The project follows basic privacy precautions during development:

- Local database files are ignored by Git.
- Test face images are not uploaded to the repository.
- Biometric files and local data folders are excluded using `.gitignore`.
- Screenshots used in reports or presentations should hide faces and private information.
- Facial encodings are treated as sensitive biometric data.
- Consent should be obtained before collecting or using face images for testing.
- Demo data should use non-sensitive or synthetic student information when possible.

Recommended future privacy improvements include:

- Database encryption
- Stronger admin authentication
- Role-based access control
- Biometric template protection
- Data deletion and retention rules
- Consent and user-management documentation

---

## How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Mohamad-101/Secure-Attendance-System-Using-Facial-Recognition.git
cd Secure-Attendance-System-Using-Facial-Recognition
```

### 2. Create and activate the Conda environment

```bash
conda create -n attendance python=3.10 -y
conda activate attendance
```

### 3. Install dlib using Conda

```bash
conda install -c conda-forge dlib -y
```

### 4. Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Optional: set an admin password

For PowerShell:

```powershell
$env:ADMIN_PASSWORD="your_secure_password"
```

If no environment variable is set, the project may use a demo password during local testing.

### 6. Run the Streamlit app

```bash
python -m streamlit run app.py
```

Using `python -m streamlit` is recommended because it runs Streamlit from the active Python environment.

---

## Requirements

The project dependencies include:

```text
streamlit
numpy
pandas
Pillow
opencv-python-headless
face-recognition
face-recognition-models
dlib
```

Because `dlib` installation can be difficult on Windows using only `pip`, Conda is recommended.

---

## Internal Testing

Internal testing was performed for the major Phase 3 workflows.

Tested cases include:

- New student enrollment
- Duplicate student ID prevention
- Duplicate face enrollment prevention
- Successful attendance verification
- Unknown face rejection
- Duplicate attendance prevention
- Failed verification logging
- Duplicate attempt logging
- Security Logs access control
- Database Status access control
- Wrong admin password logging
- Attendance filtering
- Security log filtering
- CSV exports

A detailed testing matrix is available in:

```text
docs/phase_3_security_reporting/testing_matrix.md
```

---

## Current Limitations

The current version is a local research prototype and still has the following limitations:

- The system uses captured or uploaded images rather than continuous live video.
- Full anti-spoofing and liveness detection are not implemented yet.
- Image quality validation is planned but not fully completed.
- Testing has been limited to a small number of users.
- SQLite is suitable for local development but may need to be replaced for production deployment.
- The current admin password mechanism is suitable for demonstration only.
- Recognition tolerance still needs evaluation under different lighting, pose, and environmental conditions.
- The system uses a pretrained face-recognition model rather than a custom-trained model.

---

## Next Steps

The next project phase will focus on performance, evaluation, and final preparation.

Planned work includes:

- Performance optimization and model refinement
- Evaluation under different lighting conditions
- Evaluation under different face poses
- Testing under different environmental conditions
- Image quality validation
- Dashboard usability improvements
- Privacy-safe screenshots and final documentation
- Final project report preparation
- Final presentation and demonstration preparation
- Future anti-spoofing or liveness detection

---

## Deliverables

The project contributes to the following internship deliverables:

- Secure Attendance System with Face Authentication
- Attendance Management Dashboard
- Source Code Repository
- Technical Documentation
- Attendance Reports and Analytics Module
- Internal Testing Matrix
- Weekly Progress Reports
- Technical Articles
- Presentation Slides
- Final Project Report

---

## Ethical and Academic Notes

This repository is part of the CCRI Summer Research Internship project.

When working with biometric data, the project should follow ethical AI and privacy-aware practices:

- Do not upload real face images to GitHub.
- Do not upload local database files.
- Use consent-based image collection for testing.
- Hide faces and private information in screenshots.
- Use the system for educational and research purposes only unless stronger privacy, security, and deployment controls are added.

---

## Author

**Mohamad El Saleh**  
Computer and Communication Engineering Student  
Lebanese University Faculty of Engineering  
CCRI Summer Research Internship  
Project: Secure Attendance System with Face Authentication