# User Manual

## Project

Secure Attendance System with Face Authentication

## Phase

Final Phase: Deployment, Demonstration, Documentation, and Assessment

## Week

Week 11 & 12

## Purpose

This user manual explains how to install, run, and use the Secure Attendance System with Face Authentication.

The system is designed to support face-based attendance registration, identity verification, attendance logging, reporting, and security monitoring.

---

## 1. System Overview

The Secure Attendance System is a local Streamlit application that uses face recognition to verify users and record attendance.

The system supports:

- User registration
- Face enrollment
- Face verification
- Attendance recording
- Duplicate attendance prevention
- Attendance logs and CSV export
- Security event logging
- Admin-protected monitoring pages
- Local database storage
- Privacy-safe handling of face data

The application uses a pretrained face recognition model through the `face_recognition` library. The project does not train a new deep learning model from scratch. Instead, it stores local face encodings during enrollment and compares them during verification.

---

## 2. Technologies Used

The project uses:

- Python
- Streamlit
- SQLite
- Pandas
- NumPy
- Pillow
- OpenCV
- dlib
- face_recognition

---

## 3. Project Structure

Important files and folders include:

```text
app.py
src/
├── database.py
├── face_enrollment.py
├── face_verification.py
├── attendance.py
└── access_control.py

scripts/
└── evaluate_thresholds.py

docs/
├── phase_3_security_reporting/
├── phase_4_evaluation/
└── final_submission/

data/
└── .gitkeep
```

The `data/` folder is used locally for the SQLite database. Private local database files are ignored by Git and should not be uploaded to GitHub.

---

## 4. Installation

### Step 1: Create and activate Conda environment

```powershell
conda create -n attendance python=3.10 -y
conda activate attendance
```

### Step 2: Install dlib

```powershell
conda install -c conda-forge dlib -y
```

### Step 3: Install Python requirements

```powershell
python -m pip install -r requirements.txt
```

If needed, the main required packages are:

```powershell
python -m pip install streamlit face-recognition numpy==1.26.4 pandas Pillow opencv-python-headless
```

---

## 5. Running the Application

To start the application, run:

```powershell
python -m streamlit run app.py
```

The Streamlit interface will open in the browser.

---

## 6. Main Pages

The application contains the following pages:

- System Overview
- Register User
- Verify Attendance
- View Attendance Logs
- Security Logs
- Database Status

---

## 7. System Overview Page

The System Overview page provides a summary of the project and is useful for final demonstration.

It shows:

- Main workflow
- Registered users count
- Face profiles count
- Attendance logs count
- Security logs count
- Demo guide
- Privacy reminder
- Current limitations

This page was added during the final phase to make the interface more professional and easier to present.

---

## 8. Register User

The Register User page is used to enroll a new user.

### Required inputs

- Student ID
- Full name
- Role
- Face image

### Optional input

- Email

### Image input methods

The system supports:

- Camera input
- Uploaded image input

### Enrollment process

1. Enter the student ID.
2. Enter the full name.
3. Enter the optional email.
4. Select the user role.
5. Capture or upload a clear face image.
6. Click the Enroll User button.

### Expected result

If enrollment succeeds, the system displays the enrolled user information.

The system also prevents:

- Registering the same student ID twice.
- Registering the same face under another student ID.

---

## 9. Verify Attendance

The Verify Attendance page is used to verify a face and record attendance.

### Verification process

1. Open the Verify Attendance page.
2. Capture or upload a clear face image.
3. Select the recognition tolerance.
4. The system compares the uploaded face with stored face profiles.
5. If a match is found, the system records attendance.

### Default tolerance

The default recognition tolerance is:

```text
0.60
```

A lower tolerance is stricter, while a higher tolerance is more flexible.

### Expected result

If the face is recognized:

- The system displays the matched user.
- The system displays the face distance.
- Attendance is recorded automatically.

If the same user verifies again on the same day:

- The system prevents duplicate attendance.
- A duplicate attendance security event is logged.

---

## 10. View Attendance Logs

The View Attendance Logs page is used to review attendance records.

It supports:

- Searching by student ID or name
- Filtering by date range
- Filtering by status
- Viewing summary metrics
- Exporting filtered attendance logs as CSV

### CSV export

The user can download filtered attendance records using the CSV download button.

---

## 11. Security Logs

The Security Logs page is used to monitor security-related events.

This page is protected by admin access control.

### Security events may include:

- Failed verification
- Duplicate attendance
- Enrollment errors
- No face detected
- Multiple faces detected
- Access denied attempts

### Security Logs features

The page supports:

- Filtering by event type
- Searching by student, name, or message
- Filtering by date range
- Viewing security summary metrics
- Exporting security logs as CSV

---

## 12. Database Status

The Database Status page shows local system statistics.

This page is protected by admin access control.

It displays:

- Registered users count
- Face profiles count
- Attendance logs count
- Security logs count

---

## 13. Admin Access

Sensitive pages require an admin password.

Protected pages include:

- Security Logs
- Database Status

The default local admin password is:

```text
admin123
```

For safer usage, the password can be changed using an environment variable:

```powershell
$env:ADMIN_PASSWORD="your_secure_password"
python -m streamlit run app.py
```

---

## 14. Threshold Evaluation Script

The project includes a threshold evaluation script:

```text
scripts/evaluate_thresholds.py
```

The script compares a test face image against enrolled face profiles and checks multiple tolerance values.

### Example command

```powershell
python scripts\evaluate_thresholds.py "C:\path\to\test_image.jpg"
```

### Tested tolerance values

- 0.45
- 0.50
- 0.55
- 0.60
- 0.65

This helps evaluate how strict or flexible the system is under different face image conditions.

---

## 15. Evaluation Results Summary

Example evaluation results recorded during testing:

| Condition | Face Distance | Result |
|---|---:|---|
| Good lighting | 0.3430 | Accepted |
| Low lighting | 0.4377 | Accepted |
| Bright lighting | 0.3929 | Accepted |
| Side pose | N/A | No face detected |
| Same image reused | 0.0000 | Accepted |

These results show that the system performs well with clear and front-facing images, but strong side pose can prevent face detection.

---

## 16. Privacy and Security Guidelines

Because the project uses face-related biometric data, privacy is important.

The following rules should be followed:

- Do not upload face images to GitHub.
- Do not upload local database files to GitHub.
- Do not upload biometric encodings publicly.
- Use only test data during demonstrations.
- Use another person’s face only with consent.
- Keep the SQLite database local.
- Upload only source code, documentation, and numerical evaluation results.

---

## 17. GitHub Privacy Check

Before final submission, run:

```powershell
git ls-files | Select-String -Pattern "\.jpg$|\.jpeg$|\.png$|\.db$|\.sqlite$|\.sqlite3$|face_data|test_faces|test_images|data/"
```

The only acceptable result should be:

```text
data/.gitkeep
```

This confirms that private biometric files and database files were not uploaded.

---

## 18. Common Issues

### Streamlit command not working

Use:

```powershell
python -m streamlit run app.py
```

instead of:

```powershell
streamlit run app.py
```

### Wrong environment is running

Activate the correct Conda environment:

```powershell
conda activate attendance
```

### dlib installation issue

Install dlib using Conda:

```powershell
conda install -c conda-forge dlib -y
```

### Image format issue

Use NumPy version:

```text
numpy==1.26.4
```

### No enrolled users

Register a user first before trying to verify attendance.

### No face detected

Use a clear, front-facing image with good lighting.

---

## 19. Final Demo Steps

Recommended final demo flow:

1. Open the System Overview page.
2. Register a test user.
3. Verify attendance for the enrolled user.
4. Verify the same user again to show duplicate attendance prevention.
5. Open Attendance Logs and show filters/export.
6. Open Security Logs using admin access.
7. Open Database Status using admin access.
8. Explain privacy handling and GitHub safety.

---

## 20. Current Limitations

The current system is functional, but some limitations remain:

- It works best with clear, front-facing images.
- Strong side pose may prevent face detection.
- Very poor lighting may reduce accuracy.
- Advanced liveness detection is not implemented.
- Anti-spoofing protection is not implemented.
- Testing was done using a limited local dataset.
- Deployment is local through Streamlit.

---

## 21. Future Improvements

Possible future improvements include:

- Adding liveness detection.
- Adding anti-spoofing protection.
- Supporting larger testing datasets.
- Improving mobile responsiveness.
- Adding cloud deployment.
- Adding role-based dashboards.
- Adding attendance session management.
- Adding advanced analytics and charts.

---

## 22. Final Status

The system is ready for final demonstration and final submission preparation.

The main application is functional, documented, and organized for final internship assessment.