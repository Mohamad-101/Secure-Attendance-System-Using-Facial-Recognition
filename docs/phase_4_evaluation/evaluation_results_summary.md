# Phase 4 Evaluation Results Summary

## Project
Secure Attendance System with Face Authentication

## Week
Week 10

## Objective
This document summarizes the evaluation work completed after the initial Phase 4 testing setup.

Week 9 focused on creating the threshold evaluation script and the lighting/pose testing matrix. Week 10 focuses on organizing the results, interpreting the meaning of face distances, and documenting the system’s current behavior under realistic testing conditions.

## Evaluation Method
The system was evaluated using a local threshold evaluation script. The script compares one local face image with the enrolled face profiles stored in the local SQLite database.

The tested tolerance values were:

| Tolerance | Description |
|---|---|
| 0.45 | Very strict |
| 0.50 | Strict |
| 0.55 | Balanced |
| 0.60 | Default system setting |
| 0.65 | More flexible |

## Recorded Result

| Test Case | Condition | Face Distance | Result |
|---|---|---|---|
| T01 | Clear image of enrolled user | 0.3563 | Accepted at all tested thresholds |

## Interpretation
The face distance of 0.3563 is below all tested tolerance values, including the strictest value of 0.45. This means the submitted image produced a strong match with the enrolled user profile.

This confirms that the system performs well when the input image is clear and the face is visible.

## Important Observation
If the exact same image used during enrollment is reused during verification, the face distance can be 0.0000. This is expected because the stored encoding and submitted encoding are generated from the same image.

For realistic evaluation, verification images should be different from enrollment images.

## Privacy Handling
All face images used for testing were kept locally on the testing machine. The repository contains only source code, documentation, and numerical evaluation results.

No face images, local database files, or biometric test data were uploaded to GitHub.

## Summary
Week 10 continued the Phase 4 evaluation work by documenting results and interpreting the system’s behavior under different threshold values. The system is functional, and the current evaluation helps prepare the project for final reporting and demonstration.