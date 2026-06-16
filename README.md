# Secure Attendance System with Face Authentication

**Developer:** Mohamad El Saleh

**Host Institution:** International Center for AI and Cyber Security Research and Innovations (CCRI)

**Academic Affiliation:** Lebanese University Faculty of Engineering (ULFG)

---

## Current Project Status

This repository currently represents **Phase 1** of the CCRI Secure Attendance System project.

Phase 1 focuses on:

* Literature review on facial recognition and biometric authentication systems
* Study of face detection, face recognition, and attendance management techniques
* Definition of system requirements and architecture
* Development environment setup
* Database and attendance management framework design
* Google Colab prototype testing for face encoding, distance comparison, and database operations

Full face enrollment, real-time dashboard, reporting, analytics, anti-spoofing, and deployment are planned for later phases according to the CCRI project timeline.

---

## Project Overview

Traditional attendance tracking methods are vulnerable to proxy attendance, credential sharing, manual errors, and administrative delays. This project aims to develop a secure attendance system that uses face authentication to verify a user's identity before recording attendance.

The system is designed to detect a face from an image or camera frame, generate a 128-dimensional facial encoding, compare it with stored user profiles, and record attendance after successful verification.

For the current phase, the project focuses on research, architecture design, database planning, and prototype validation rather than full production deployment.

---

## Repository Architecture & Navigation

This repository is organized into documentation, prototype testing, and setup files.

* 📂 **[`/docs`](./docs)** — Project documentation and system design.

  * [`PHASE_1_DOCUMENTATION.md`](./docs/PHASE_1_DOCUMENTATION.md): Phase 1 research summary, requirements, architecture, database design, and attendance framework.

* 📂 **[`/research_sandbox`](./research_sandbox)** — Google Colab / Jupyter prototype testing.

  * [`Phase1_Vision_and_DB_Tests.ipynb`](./research_sandbox/Phase1_Vision_and_DB_Tests.ipynb): Phase 1 prototype notebook for face encoding, distance comparison, SQLite table creation, and demo attendance log insertion.

---

## Core Technology Stack

* **Language:** Python
* **Computer Vision:** OpenCV
* **Face Recognition:** dlib / `face_recognition`
* **Face Representation:** 128-dimensional facial embeddings
* **Database:** SQLite
* **Data Handling:** NumPy, Pandas
* **Prototype Environment:** Google Colab / Jupyter Notebook
* **Planned Interface:** Streamlit

---

## Development Environment

The Phase 1 prototype was developed and tested using Google Colab. This was chosen because face recognition libraries such as `dlib` and `face_recognition` may require additional setup or stronger hardware on local machines.

To install the project dependencies, use:

```bash
pip install -r requirements.txt
```

---

## Project Development Roadmap

The project is being developed in structured phases throughout the internship.

### Phase 1: Research, Architecture, and Prototype Testing

* [x] Review facial recognition and biometric authentication concepts
* [x] Study face detection, face recognition, and attendance management techniques
* [x] Define system requirements and architecture
* [x] Set up the development environment
* [x] Design the SQLite database and attendance framework
* [x] Test face encoding and distance comparison in Google Colab
* [x] Insert demo user, facial profile, demo session, and attendance log records

### Phase 2: Enrollment, Verification, and Dashboard

* [ ] Build user enrollment and facial profile registration module
* [ ] Move notebook logic into reusable Python modules
* [ ] Implement attendance recording after successful verification
* [ ] Add duplicate check-in prevention
* [ ] Start Streamlit dashboard interface

### Phase 3: Security, Reporting, and Evaluation

* [ ] Add basic attendance report generation
* [ ] Implement CSV export
* [ ] Evaluate recognition results under different lighting and pose conditions
* [ ] Study and implement anti-spoofing improvements
* [ ] Improve access control and data protection

---

## Privacy and Data Handling

Facial data is sensitive biometric information. Test images and local database files should not be uploaded to the repository.

The `.gitignore` file excludes image files, local databases, virtual environments, and notebook checkpoints to reduce the risk of exposing private test data.

---

## Notes

This repository currently contains Phase 1 work only. The full application, dashboard, reporting module, anti-spoofing features, and deployment will be developed in later phases.
