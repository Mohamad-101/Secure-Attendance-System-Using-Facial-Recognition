# Secure Attendance System Using Facial Recognition

## Project Overview

This project is a research internship implementation of a secure attendance system using face authentication.

The system allows users to register with a face image, verify their identity using facial recognition, record attendance automatically, view attendance reports, monitor security events, and protect sensitive dashboard pages with admin access control.

The project was developed as part of the CCRI Summer Research Internship under the theme:

**Secure Attendance System with Face Authentication**

---

## Current Project Status

The project has progressed beyond the initial MVP stage and is currently in the evaluation and final preparation phase.

Completed phases include:

| Phase   | Status      | Main Work                                                                          |
| ------- | ----------- | ---------------------------------------------------------------------------------- |
| Phase 1 | Completed   | Literature review, requirements, system architecture, database planning            |
| Phase 2 | Completed   | Face enrollment, face verification, attendance recording, Streamlit dashboard      |
| Phase 3 | Completed   | Reporting, security logging, admin access control, duplicate enrollment prevention |
| Phase 4 | In Progress | Threshold evaluation, lighting/pose testing, system limitations, final preparation |

---

## Main Features

### User Enrollment

* Register users with student ID, full name, email, and role.
* Upload or capture a face image.
* Generate and store facial encodings locally.
* Prevent duplicate student ID enrollment.
* Prevent duplicate face enrollment under a different ID.

### Face Verification

* Verify a submitted face image against enrolled facial profiles.
* Use face distance comparison for identity matching.
* Adjustable recognition tolerance in the Streamlit interface.
* Reject unknown users.

### Attendance Recording

* Automatically record attendance after successful verification.
* Prevent duplicate attendance for the same user on the same day.
* Store attendance logs in a local SQLite database.

### Attendance Reports

* View attendance records in a dashboard.
* Filter by student ID, name, date, and status.
* Export filtered attendance logs as CSV.

### Security Logs

* Log failed verification attempts.
* Log duplicate attendance attempts.
* Log enrollment errors.
* Log invalid admin access attempts.
* View and filter security logs from the dashboard.
* Export security logs as CSV.

### Admin Access Control

* Protect sensitive pages such as Security Logs and Database Status.
* Require an admin password before allowing access.
* Log failed admin password attempts as security events.

### Evaluation Tools

* Local threshold evaluation script.
* Tests multiple tolerance values: 0.45, 0.50, 0.55, 0.60, and 0.65.
* Records face distance and accept/reject behavior.
* Supports Phase 4 lighting, pose, and environment testing.

---

## Technical Approach

This project uses the `face_recognition` Python library with dlib’s pretrained face recognition model.

The system does **not** train a custom ResNet model from scratch. Instead, it uses a pretrained ResNet-based face embedding model to generate 128-dimensional facial encodings.

Project-specific “training” is handled through enrollment, where each user’s facial encoding is stored in the local database and later compared during verification.

---

## Tech Stack

| Component            | Technology             |
| -------------------- | ---------------------- |
| Programming Language | Python                 |
| Web Interface        | Streamlit              |
| Face Recognition     | face_recognition, dlib |
| Image Processing     | Pillow, OpenCV         |
| Database             | SQLite                 |
| Data Handling        | pandas, NumPy          |
| Version Control      | Git and GitHub         |

---

## Repository Structure

```text
Secure-Attendance-System-Using-Facial-Recognition/
│
├── app.py
├── README.md
├── requirements.txt
│
├── src/
│   ├── attendance.py
│   ├── database.py
│   ├── face_enrollment.py
│   ├── face_verification.py
│   ├── access_control.py
│   └── __init__.py
│
├── scripts/
│   └── evaluate_thresholds.py
│
├── docs/
│   ├── phase_3_security_reporting/
│   └── phase_4_evaluation/
│
└── data/
    └── attendance.db
```

Local database files and biometric data should remain private and should not be uploaded to GitHub.

---

## Main Files

| File                             | Purpose                                         |
| -------------------------------- | ----------------------------------------------- |
| `app.py`                         | Main Streamlit dashboard                        |
| `src/database.py`                | SQLite database setup and database operations   |
| `src/face_enrollment.py`         | User enrollment and duplicate enrollment checks |
| `src/face_verification.py`       | Face verification and distance matching         |
| `src/attendance.py`              | Attendance recording logic                      |
| `src/access_control.py`          | Admin access protection for sensitive pages     |
| `scripts/evaluate_thresholds.py` | Local threshold evaluation script               |

---

## Database Tables

The system uses a local SQLite database with tables for:

| Table                 | Purpose                            |
| --------------------- | ---------------------------------- |
| `users`               | Stores registered user information |
| `facial_profiles`     | Stores facial encodings            |
| `attendance_sessions` | Stores attendance session data     |
| `attendance_logs`     | Stores attendance records          |
| `security_logs`       | Stores security-related events     |

---

## Face Verification Logic

During verification, the system compares the submitted face encoding with stored face encodings.

The closest match is selected based on face distance.

A lower distance means a stronger match.

Default tolerance:

```text
0.60
```

Example interpretation:

| Face Distance | Meaning                                       |
| ------------- | --------------------------------------------- |
| 0.0000        | Exact same image or nearly identical encoding |
| 0.30 – 0.45   | Strong match                                  |
| 0.45 – 0.60   | Possible match depending on tolerance         |
| Above 0.60    | Usually rejected                              |

---

## Phase 4 Evaluation

Phase 4 focuses on testing and evaluating the system under realistic conditions.

The evaluation includes:

* Threshold testing
* Lighting condition testing
* Pose variation testing
* Distance analysis
* False acceptance and false rejection observations
* Privacy-safe testing documentation

The evaluation script can be run locally using:

```powershell
python scripts\evaluate_thresholds.py "C:\path\to\test_image.jpg"
```

Face images used for testing must remain local and should not be committed to GitHub.

---

## Privacy and Ethical Handling

This project handles biometric-related data, so privacy is important.

The following rules are followed:

* Face images are kept local.
* SQLite database files are not uploaded to GitHub.
* Biometric encodings are stored only in the local database.
* Public documentation uses numerical results and observations, not personal face images.
* Testing with another person should only be done with consent.

---

## How to Run Locally

### 1. Clone the repository

```powershell
git clone https://github.com/Mohamad-101/Secure-Attendance-System-Using-Facial-Recognition.git
cd Secure-Attendance-System-Using-Facial-Recognition
```

### 2. Create and activate Conda environment

```powershell
conda create -n attendance python=3.10 -y
conda activate attendance
```

### 3. Install dependencies

```powershell
conda install -c conda-forge dlib -y
python -m pip install face-recognition streamlit numpy pandas Pillow opencv-python-headless
```

### 4. Run the Streamlit app

```powershell
python -m streamlit run app.py
```

---

## Current Completed Work

* Project structure created.
* SQLite database implemented.
* Face enrollment implemented.
* Face verification implemented.
* Attendance recording implemented.
* Duplicate attendance prevention implemented.
* Attendance dashboard implemented.
* Attendance CSV export implemented.
* Security logging implemented.
* Security Logs dashboard implemented.
* Admin access control implemented.
* Duplicate student ID prevention implemented.
* Duplicate face enrollment prevention implemented.
* Phase 4 threshold evaluation script added.
* Lighting and pose testing documentation added.

---

## Current Limitations

* The system works best with clear, front-facing images.
* Poor lighting or strong pose variation may affect recognition.
* Uploading the exact enrollment image can produce a face distance of 0.0000.
* Advanced liveness detection is not yet implemented.
* Evaluation is still based on a small local test set.

---

## Future Improvements

* Add image quality validation.
* Add pose validation.
* Add liveness detection or anti-spoofing checks.
* Expand testing with more participants and conditions.
* Improve final deployment and demo setup.
* Prepare final internship report and user manual.

---

## Author

**Mohamad El Saleh**
Computer and Communication Engineering
Lebanese University Faculty of Engineering
Remote Research Intern – CCRI
