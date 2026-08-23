# System Limitations and Future Improvements

## Project
Secure Attendance System with Face Authentication

## Week
Week 10

## Purpose
This document summarizes the current limitations observed during evaluation and lists possible future improvements for the Secure Attendance System.

## Current Strengths
The system currently supports:

| Feature | Status |
|---|---|
| User enrollment | Implemented |
| Face verification | Implemented |
| Attendance recording | Implemented |
| Duplicate attendance prevention | Implemented |
| Attendance dashboard | Implemented |
| Security logs | Implemented |
| Admin access control | Implemented |
| Duplicate student ID prevention | Implemented |
| Duplicate face enrollment prevention | Implemented |
| Threshold evaluation script | Implemented |

## Current Limitations

### 1. Image Quality Dependence
The system works best with clear, front-facing images. Poor lighting, blur, or overexposure may reduce reliability.

### 2. Pose Sensitivity
Side-facing or tilted images may increase face distance or cause detection failure.

### 3. Same Image Reuse
If the same enrollment image is uploaded again during verification, the distance can become 0.0000. This is technically expected, but real attendance should prefer camera capture.

### 4. Limited Evaluation Dataset
The current evaluation uses a small local test set. A larger dataset with more participants would improve the reliability of the analysis.

### 5. No Advanced Liveness Detection
The current system does not yet include advanced anti-spoofing or liveness detection.

## Future Improvements

| Improvement | Purpose |
|---|---|
| Image quality validation | Detect blurry, dark, or overexposed images |
| Pose validation | Detect non-frontal or tilted faces |
| Liveness detection | Reduce spoofing risk |
| Larger test dataset | Improve evaluation reliability |
| FAR / FRR analysis | Measure false acceptance and false rejection |
| Camera-only verification mode | Reduce reused-image risk |
| Final demo checklist | Prepare controlled final presentation |

## Summary
The current system satisfies the main functional requirements of the internship project. The remaining limitations are mainly related to robustness, real-world testing, and future security improvements.