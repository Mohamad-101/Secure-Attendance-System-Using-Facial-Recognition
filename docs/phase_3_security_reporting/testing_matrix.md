# Phase 3 Testing Matrix

## Project: Secure Attendance System with Face Authentication

This document summarizes the internal testing performed during Phase 3 of the project. The goal of this phase is to verify that the system works correctly after adding reporting, security logging, access control, and enrollment validation features.

---

## 1. Enrollment Testing

| Test Case | Expected Result | Status |
|---|---|---|
| Register a new student with a new face image | Student is enrolled successfully | Passed |
| Register the same student ID again | Enrollment is blocked because the student ID already exists | Passed |
| Register a different student ID using an already enrolled face | Enrollment is blocked because the face is already enrolled | Passed |
| Register with no face in the image | Enrollment is rejected and an error message is shown | To Test |
| Register with multiple faces in the image | Enrollment is rejected and an error message is shown | To Test |

---

## 2. Attendance Verification Testing

| Test Case | Expected Result | Status |
|---|---|---|
| Verify attendance using a registered face | User is recognized and attendance is recorded | Passed |
| Verify attendance again using the same user on the same day | Duplicate attendance is blocked | Passed |
| Verify attendance using an unknown face | Face is rejected because it does not match enrolled users | Passed |
| Verify attendance with no face detected | Verification is rejected and logged as a security event | To Test |
| Verify attendance with multiple faces detected | Verification is rejected and logged as a security event | To Test |

---

## 3. Security Logging Testing

| Test Case | Expected Result | Status |
|---|---|---|
| Failed face verification attempt | Event is saved in Security Logs | Passed |
| Duplicate attendance attempt | Event is saved in Security Logs | Passed |
| No face detected | Event is saved in Security Logs | To Test |
| Multiple faces detected | Event is saved in Security Logs | To Test |
| Wrong admin password attempt | Event is saved as ACCESS_DENIED | Passed |

---

## 4. Access Control Testing

| Test Case | Expected Result | Status |
|---|---|---|
| Open Security Logs without password | Page is blocked | Passed |
| Open Security Logs with wrong password | Access is denied and event is logged | Passed |
| Open Security Logs with correct password | Page opens successfully | Passed |
| Open Database Status without password | Page is blocked | Passed |
| Open Database Status with correct password | Page opens successfully | Passed |

---

## 5. Reporting and Export Testing

| Test Case | Expected Result | Status |
|---|---|---|
| Filter attendance logs by student/name | Filtered records are displayed correctly | Passed |
| Filter attendance logs by date range | Filtered records are displayed correctly | Passed |
| Export attendance logs as CSV | CSV file is generated successfully | Passed |
| Filter security logs by event type | Filtered events are displayed correctly | Passed |
| Search security logs by student/name/message | Matching events are displayed correctly | Passed |
| Export security logs as CSV | CSV file is generated successfully | Passed |

---

## 6. Final Notes

The main Phase 3 functionality has been tested successfully. The system now includes attendance reporting, security event logging, admin access control for sensitive pages, and duplicate enrollment prevention.

Remaining improvements for the next phase include performance optimization, lighting and pose evaluation, image quality validation, and future anti-spoofing or liveness detection.