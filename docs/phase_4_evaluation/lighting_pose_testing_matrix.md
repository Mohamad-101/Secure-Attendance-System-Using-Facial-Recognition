# Lighting and Pose Testing Matrix

## Project

Secure Attendance System with Face Authentication

## Phase

Phase 4: Evaluation, Optimization, and Model Refinement

## Objective

This document records how the Secure Attendance System behaves under different lighting and face pose conditions.

The goal of this test is not to compare multiple threshold values. Threshold comparison is documented separately in `threshold_testing_plan.md`. This matrix focuses only on how image capture conditions affect face detection, face distance, and verification behavior.

---

## 1. Testing Scope

The lighting and pose tests were performed using the default system tolerance value:

```text
0.60
```

This value was used because it represents the main practical setting of the attendance system during verification.

The test focuses on the following questions:

- Can the system detect the face under different conditions?
- Does the face distance increase when lighting becomes worse?
- Can the user still be verified at the default tolerance?
- Which image conditions cause detection or verification failure?

---

## 2. Testing Conditions

| Condition ID | Condition | Description | Expected Behavior |
|---|---|---|---|
| L01 | Good lighting | Clear indoor lighting with a front-facing face | Face should be detected and verified |
| L02 | Low lighting | Weak or dim lighting condition | Face distance may increase or verification may become less reliable |
| L03 | Bright lighting | Strong lighting or overexposed image | Face distance may increase or detection may be affected |
| L04 | Side pose | Face turned left or right | Face detection may fail or verification may become less reliable |

---

## 3. Recorded Test Results

The following results were recorded using local test images and the threshold evaluation script.

| Test ID | Condition | Student/User | Tolerance | Face Distance | Actual Result | Status | Notes |
|---|---|---|---|---|---|---|---|
| T01 | Good lighting | T001 / Test User | 0.60 | 0.4621 | Accepted | Pass | Clear front-facing image accepted at the default tolerance |
| T02 | Low lighting | T001 / Test User | 0.60 | 0.5176 | Accepted | Pass | Distance increased under low lighting but remained below 0.60 |
| T03 | Bright lighting | T001 / Test User | 0.60 | 0.4878 | Accepted | Pass | Bright lighting still allowed successful verification |
| T04 | Side pose | T001 / Test User | 0.60 | N/A | No face detected | Observed limitation | Side pose affected face detection |

---

## 4. Result Interpretation

The results show that the system works best with clear, front-facing images. Under good lighting, the system detected the face and verified the user successfully with a face distance of `0.4621`.

Low lighting increased the face distance to `0.5176`, which means the match became weaker. However, the distance was still below the default tolerance value of `0.60`, so the user was accepted.

Bright lighting produced a face distance of `0.4878`. The user was still accepted, showing that the system can handle some lighting variation when the face remains visible.

The side pose image caused face detection failure. This shows that the current system is sensitive to face orientation and works better when the user faces the camera directly.

---

## 5. Evaluation Summary

The lighting and pose evaluation showed that:

- Good lighting allowed successful verification.
- Low lighting increased the face distance but was still accepted.
- Bright lighting was accepted at the default tolerance.
- Side pose caused face detection failure.
- The system performs best with clear, front-facing images.
- The default tolerance value of `0.60` was practical for the tested lighting conditions.

---

## 6. Practical Recommendation

For reliable attendance verification, users should provide a clear, front-facing image with acceptable lighting.

Recommended capture conditions:

| Recommendation | Reason |
|---|---|
| Face the camera directly | Reduces face detection failure |
| Use clear indoor lighting | Improves face detection and matching |
| Avoid very dark images | Low lighting increases face distance |
| Avoid strong overexposure | Bright images may affect recognition quality |
| Keep the full face visible | Partial or side-facing images may fail detection |

---

## 7. Privacy Handling

All test images were kept locally on the testing machine.

Privacy precautions included:

- Test face images were not uploaded to GitHub.
- Local SQLite database files were not uploaded to GitHub.
- Biometric encodings and test data were kept private.
- Only numerical results were recorded in the documentation.
- The evaluation process remained local and privacy-aware.

---

## 8. Conclusion

This testing matrix shows how lighting and pose affect the Secure Attendance System during verification.

The system successfully verified the enrolled user under good, low, and bright lighting conditions using the default tolerance value of `0.60`. However, the side pose test showed a limitation because no face was detected.

These results support the Phase 4 evaluation by showing that the system is functional under clear image conditions, while also identifying pose sensitivity as a practical limitation for future improvement.