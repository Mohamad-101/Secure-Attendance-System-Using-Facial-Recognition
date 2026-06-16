## Current Project Status

This repository currently represents Phase 1 of the CCRI Secure Attendance System project.

Phase 1 focuses on:
- Literature review on facial recognition and biometric authentication systems
- Study of face detection, face recognition, and attendance management techniques
- Definition of system requirements and architecture
- Development environment setup
- Database and attendance management framework design

Full face enrollment, real-time dashboard, reporting, analytics, and deployment are planned for later phases according to the CCRI project timeline.

# Secure Attendance System with Face Authentication

**Developer:** Mohamad El Saleh  
**Host Institution:** International Center for AI and Cyber Security Research and Innovations (CCRI)  
**Academic Affiliation:** Lebanese University Faculty of Engineering (ULFG)  

---

##  Project Overview
Traditional attendance tracking methods are highly vulnerable to proxy fraud, physical credential cloning, and administrative lag. This project is a highly secure, automated attendance infrastructure being developed as a research deliverable for the CCRI Global Research Internship Program. 

The system enforces identity verification through deep-learning biometric profiling (ResNet-68), edge-based facial localization, and atomic relational database state tracking.

---

##  Repository Architecture & Navigation
This repository is strictly organized to isolate system documentation, isolated prototype testing, and production runtime environments.

* 📂 **[`/docs`](./docs)** — Core system engineering blueprints.
  * [`PHASE_1_DOCUMENTATION.md`](./docs/PHASE_1_DOCUMENTATION.md): Complete system requirements, architecture topology, and SQLite3 entity-relationship diagrams.
* 📂 **[`/research_sandbox`](./research_sandbox)** — Isolated Jupyter environments for proof-of-concept testing.
  * [`Phase1_Vision_and_DB_Tests.ipynb`](./research_sandbox/Phase1_Vision_and_DB_Tests.ipynb): Validated biometric ingestion pipelines and parameterized database initialization scripts.

---

##  Core Technology Stack
* **Language:** Python 3.12
* **Computer Vision:** OpenCV, dlib (Histogram of Oriented Gradients)
* **Deep Learning:** ResNet-68 (128-D Facial Vector Embeddings)
* **Data Persistence:** SQLite3 (Relational Schema & JSON Serialization)
* **Presentation Layer:** Streamlit with WebRTC (Upcoming)

---

##  Project Development Roadmap
This infrastructure is being built in structured phases over the internship lifecycle.

### Phase 1: Biometric Engine & Database Design
- [x] Select and validate HOG + SVM face localization pipeline.
- [x] Configure ResNet-68 feature extraction array (128-D).
- [x] Design multi-table SQLite relational schema with cascading deletions.
- [x] Finalize system architecture documentation.

### Phase 2: Web Interface & Real-Time Analytics
- [ ] Initialize Streamlit frontend scaffolding.
- [ ] Integrate WebRTC camera ingestion streams.
- [ ] Connect presentation layer to backend verification metrics.

### Phase 3: Edge Case Mitigation & Reporting
- [ ] Implement anti-spoofing security fallbacks.
- [ ] Develop automated CSV administrative reporting.
