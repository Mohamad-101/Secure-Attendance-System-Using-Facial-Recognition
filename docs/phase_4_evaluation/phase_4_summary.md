# Secure Attendance System with Face Authentication

## Phase 4 Documentation: Evaluation, Optimization, and Model Refinement

**Developer:** Mohamad El Saleh  
**Host Institution:** International Center for AI and Cyber Security Research and Innovations (CCRI)  
**Academic Affiliation:** Lebanese University – Faculty of Engineering  
**Phase:** Phase 4 — Evaluation, Optimization, and Model Refinement  
**Timeline:** August 1 – August 15  

---

## 1. Phase 4 Overview

Phase 4 focused on evaluating the Secure Attendance System after the main implementation, reporting, security logging, and access control features were completed.

The goal of this phase was to test how the face verification workflow behaves under different tolerance values and realistic image conditions. This included threshold testing, lighting and pose testing, result interpretation, limitation analysis, and future improvement planning.

The system uses a pretrained `dlib` / `face_recognition` model to generate 128-dimensional face encodings. The project does not train a custom ResNet model from scratch. Instead, refinement is performed through threshold testing, face distance analysis, and evaluation under different image conditions.

---

## 2. Phase 4 Objectives

The main objectives of Phase 4 were:

- Evaluate different face recognition tolerance values.
- Analyze how face distance affects verification decisions.
- Test the system under different lighting conditions.
- Test the system with different face pose conditions.
- Identify cases where face detection or verification may fail.
- Document the effect of image quality on verification reliability.
- Summarize current system strengths and limitations.
- Propose future improvements for robustness and security.
- Prepare evaluation material for the final report and demonstration.

---

## 3. Phase 4 Documentation Files

The Phase 4 work is organized into several focused documentation files.

| Document | Purpose |
|---|---|
| `threshold_testing_plan.md` | Documents the threshold testing method and the effect of different tolerance values |
| `lighting_pose_testing_matrix.md` | Records how lighting and face pose affect detection and verification |
| `evaluation_results_summary.md` | Summarizes the main recorded evaluation results |
| `system_limitations_and_improvements.md` | Lists current strengths, limitations, and future improvements |

This summary file provides the overall Phase 4 overview, while the other files contain the detailed evaluation records.

---

## 4. Evaluation Work Completed

During Phase 4, the system was evaluated using local test images and the threshold evaluation script:

```text
scripts/evaluate_thresholds.py
```

The evaluation focused on:

- Testing different tolerance values.
- Recording face distance values.
- Checking whether valid users were accepted or rejected.
- Observing the effect of lighting changes.
- Observing the effect of side pose.
- Identifying practical limitations of the current prototype.

All evaluation images and biometric-related data were kept locally and were not uploaded to GitHub.

---

## 5. Threshold Evaluation Summary

The threshold evaluation tested how different tolerance values affect verification decisions.

The tested tolerance values were:

```text
0.45, 0.50, 0.55, 0.60, 0.65
```

The default tolerance value used by the main system is:

```text
0.60
```

A lower tolerance value makes the system stricter, while a higher tolerance value makes it more flexible. The evaluation showed that very strict values may reject valid users, especially when lighting conditions are not ideal.

---

## 6. Recorded Evaluation Summary

The main recorded results are summarized below.

| Test Case | Condition | Face Distance | Result at 0.60 | Observation |
|---|---|---|---|---|
| T01 | Good lighting | 0.4621 | Accepted | Clear front-facing image worked correctly |
| T02 | Low lighting | 0.5176 | Accepted | Distance increased but remained acceptable |
| T03 | Bright lighting | 0.4878 | Accepted | Verification still succeeded |
| T04 | Side pose | N/A | No face detected | Face orientation affected detection |

These results show that the system performs best with clear, front-facing images. The default tolerance value of `0.60` was practical for the tested lighting conditions.

---

## 7. Results Interpretation

The evaluation confirmed that the system can verify an enrolled user under good, low, and bright lighting conditions using the default tolerance value.

Good lighting produced the most reliable behavior. Low lighting increased the face distance, which means the match became weaker, but the user was still accepted. Bright lighting was also accepted, although lighting changes can still affect recognition quality.

The side pose test resulted in no face being detected. This shows that the current system is sensitive to face orientation and works better when the user faces the camera directly.

---

## 8. Current System Strengths

By the end of Phase 4, the system supported the main functional requirements of the project.

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

These features show that the system had moved beyond a basic MVP and became a functional local attendance system with verification, reporting, monitoring, and evaluation support.

---

## 9. Main Limitations Observed

Phase 4 also identified several practical limitations.

| Limitation | Explanation |
|---|---|
| Image quality dependence | The system works best with clear, front-facing images |
| Pose sensitivity | Side-facing images may fail detection |
| Limited evaluation dataset | Testing was performed using a small local test set |
| No advanced liveness detection | The system does not yet detect spoofing attempts such as printed photos or replayed images |
| Local database only | SQLite is suitable for prototype development but not large-scale deployment |
| No database encryption yet | Stored biometric encodings are not encrypted in the prototype |

These limitations do not prevent the prototype from functioning, but they identify areas that should be improved in future versions.

---

## 10. Privacy Handling During Evaluation

Privacy was considered during Phase 4 because face data is sensitive biometric information.

The following precautions were followed:

- Test face images were kept locally.
- Face images were not uploaded to GitHub.
- Local SQLite database files were not uploaded to GitHub.
- Biometric encodings and test data were kept private.
- Only numerical evaluation results were recorded in documentation.
- `.gitignore` was used to exclude sensitive local files.

This approach supports privacy-aware academic evaluation and protects sensitive biometric data during development.

---

## 11. Phase 4 Outcome

Phase 4 successfully evaluated the Secure Attendance System under different tolerance values and image conditions.

The main outcomes of Phase 4 were:

- A threshold testing plan was prepared.
- A lighting and pose testing matrix was created.
- Evaluation results were recorded and summarized.
- The meaning of face distance values was documented.
- The default tolerance value of `0.60` was found to be practical for the tested conditions.
- Pose sensitivity was identified as an important limitation.
- Current system strengths and limitations were documented.
- Future improvements were proposed.

By the end of Phase 4, the system had a clearer evaluation record and was better prepared for final reporting, demonstration, and submission.

---

## 12. Next Steps for Final Phase

The final phase should focus on preparing the project for submission and demonstration.

Planned final phase tasks include:

- Improve the final user interface.
- Prepare the final user manual.
- Prepare the final deliverables checklist.
- Organize the GitHub repository.
- Verify that private images and database files are ignored by Git.
- Prepare the final project report.
- Prepare the final presentation slides.
- Prepare a controlled final demo.
- Summarize the complete internship work and final system status.

---