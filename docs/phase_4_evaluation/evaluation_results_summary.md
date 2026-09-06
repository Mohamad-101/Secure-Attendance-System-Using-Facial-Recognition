# Phase 4 Evaluation Results Summary

## Project

Secure Attendance System with Face Authentication

## Phase

Phase 4: Evaluation, Optimization, and Model Refinement

## Objective

This document summarizes the main evaluation results of the Secure Attendance System during Phase 4.

Detailed threshold testing is documented in `threshold_testing_plan.md`, while detailed lighting and pose testing is documented in `lighting_pose_testing_matrix.md`. This file only presents the final summarized results and main observations.

---

## 1. Evaluation Summary

The system was evaluated using local test images and the threshold evaluation script:

```text
scripts/evaluate_thresholds.py
```

The evaluation focused on:

- Face distance values
- Acceptance or rejection at different tolerance levels
- Behavior under different lighting conditions
- Behavior under side-pose conditions

The default tolerance used by the main application is:

```text
0.60
```

---

## 2. Final Recorded Results

| Test Case | Condition | Face Distance | Result at 0.60 | Observation |
|---|---|---|---|---|
| T01 | Good lighting | 0.4621 | Accepted | Clear front-facing image worked correctly |
| T02 | Low lighting | 0.5176 | Accepted | Distance increased but remained acceptable |
| T03 | Bright lighting | 0.4878 | Accepted | Verification still succeeded |
| T04 | Side pose | N/A | No face detected | Side pose affected face detection |

---

## 3. Main Observations

The evaluation showed that the system works best when the user provides a clear, front-facing face image.

Good lighting gave the most reliable verification behavior. Low lighting increased the face distance, meaning the match became weaker, but the user was still accepted at the default tolerance value of `0.60`.

Bright lighting was also accepted, although lighting changes can still affect recognition quality. The side pose test failed because no face was detected, showing that the current system is sensitive to face orientation.

Overall, the default tolerance value of `0.60` was practical for the tested conditions.

---

## 4. Same Image Reuse Note

If the exact same image used during enrollment is reused during verification, the face distance may become:

```text
0.0000
```

This is expected because both encodings come from the same image. However, this is not realistic for real attendance verification. A proper test should use a different verification image, preferably captured live using the camera.

---

## 5. Privacy Handling

All testing was performed locally.

Privacy precautions included:

- Test face images were not uploaded to GitHub.
- Local database files were not uploaded to GitHub.
- Biometric encodings and test data were kept private.
- Only numerical results were recorded in documentation.

---

## 6. Conclusion

Phase 4 evaluation confirmed that the Secure Attendance System can verify an enrolled user under good, low, and bright lighting conditions using the default tolerance value of `0.60`.

The main practical limitation observed was pose sensitivity, since the side-pose test resulted in no face detection. Future improvements should focus on better image quality validation, pose handling, larger testing datasets, and liveness detection.