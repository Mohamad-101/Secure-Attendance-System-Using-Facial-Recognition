# Lighting and Pose Testing Matrix

## Project
Secure Attendance System with Face Authentication

## Phase
Phase 4: Evaluation, Optimization, and Model Refinement

## Objective
This document records system behavior under different lighting, pose, and environmental conditions.

The goal is to evaluate whether the attendance verification workflow remains reliable when face images are captured in realistic conditions.

## Testing Conditions

| Condition ID | Condition | Description | Expected Behavior |
|---|---|---|---|
| L01 | Good lighting | Clear indoor lighting, front-facing face | Face should be detected and verified |
| L02 | Low lighting | Dark room or weak light | Detection or verification may fail |
| L03 | Bright lighting | Strong light or overexposed image | Detection may be affected |
| L04 | Side pose | Face turned left or right | Face may not be detected or distance may increase |
| L05 | Tilted face | Head tilted upward, downward, or sideways | Verification may become less reliable |
| L06 | Far from camera | Face appears small in image | Detection may fail |
| L07 | Close to camera | Face too close or partially cropped | Detection may fail |
| L08 | Background variation | Different room/background | Should not affect verification significantly |
| L09 | Same enrollment image reused | Exact same image used for enrollment and verification | Distance may be 0.0000 |
| L10 | Unknown user | Face not enrolled in database | System should reject |

## Test Results Table

| Test ID | Condition | Student/User | Tolerance | Face Distance | Actual Result | Expected Result | Pass/Fail | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | Good lighting |  | 0.60 |  |  | Accepted |  |  |
| 2 | Low lighting |  | 0.60 |  |  | May reject |  |  |
| 3 | Bright lighting |  | 0.60 |  |  | May reject |  |  |
| 4 | Side pose |  | 0.60 |  |  | May reject |  |  |
| 5 | Unknown user |  | 0.60 |  |  | Rejected |  |  |
| 6 | Same image reused |  | 0.60 | 0.0000 |  | Accepted |  | Expected if exact same image is reused |

## Important Observation
If the same image used during enrollment is uploaded again during verification, the face distance can be 0.0000. This is expected because the stored encoding and submitted encoding come from the same image.

For realistic attendance testing, the verification image should be different from the enrollment image.

## Evaluation Goal
This testing matrix will help identify practical limitations of the current system and document how lighting, pose, and image capture conditions affect verification performance.