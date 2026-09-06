# Secure Attendance System with Face Authentication

## Phase 3 Documentation: Reporting, Security Logging, Access Control, and Internal Testing

**Developer:** Mohamad El Saleh  
**Host Institution:** International Center for AI and Cyber Security Research and Innovations (CCRI)  
**Academic Affiliation:** Lebanese University – Faculty of Engineering  
**Phase:** Phase 3 — Reporting, Security Logging, Access Control, and Internal Testing  
**Timeline:** July 11 – July 31  

---

## 1. Phase 3 Overview

Phase 3 focused on improving the Secure Attendance System after the first working MVP was completed in Phase 2. While Phase 2 provided the main enrollment, verification, attendance recording, and dashboard features, Phase 3 moved the project toward a more secure, monitored, and testable system.

The main focus of this phase was to improve reporting, add security event logging, protect sensitive dashboard pages, prevent duplicate enrollment attempts, and perform internal testing on the main workflows. These improvements helped prepare the system for later evaluation, optimization, and final documentation.

During Phase 3, the project moved from a basic functional MVP into a more complete prototype with better monitoring and stronger data integrity.

---

## 2. Phase 3 Objectives

The main objectives of Phase 3 were:

- Improve attendance reporting and analytics.
- Add filtering and search features for attendance logs.
- Allow attendance records to be exported as CSV files.
- Add a security logging system for failed, duplicate, or suspicious events.
- Create a Security Logs dashboard page.
- Protect sensitive pages using basic admin access control.
- Log wrong admin password attempts.
- Prevent duplicate student registration.
- Prevent the same face from being enrolled using a different student ID.
- Perform internal testing for enrollment, verification, attendance, security logs, and CSV export.
- Prepare the system for later threshold evaluation, reliability testing, and final optimization.

---

## 3. Implemented Phase 3 Features

| Feature | Description | Status |
|---|---|---|
| Attendance reporting | Improved attendance log viewing and filtering | Completed |
| Attendance analytics | Added summary metrics for attendance records | Completed |
| CSV export | Added export support for filtered attendance logs | Completed |
| Security logging | Added logging for failed, duplicate, and suspicious events | Completed |
| Security Logs page | Added dashboard page for reviewing security events | Completed |
| Admin access control | Protected sensitive monitoring pages | Completed |
| Access denied logging | Logged wrong admin password attempts | Completed |
| Duplicate student ID prevention | Blocked repeated registration using the same student ID | Completed |
| Duplicate face prevention | Blocked enrolling the same face under another student ID | Completed |
| Internal testing | Tested main workflows and security-related cases | Completed |

---

## 4. Attendance Reporting and Analytics

The attendance dashboard was improved to make attendance records easier to review, filter, and export. This helped make the system more useful for administrators or evaluators who need to inspect attendance activity.

Implemented attendance reporting features include:

- Viewing attendance logs in a dashboard table.
- Searching attendance records by student ID or full name.
- Filtering attendance records by date range.
- Filtering attendance records by attendance status.
- Displaying attendance summary metrics.
- Exporting filtered attendance records as a CSV file.

These features improved the usability of the system and made attendance data easier to analyze.

---

## 5. Security Logging

A security logging module was added to track failed, duplicate, and suspicious system events. This feature improves system traceability and helps during debugging, testing, and security monitoring.

The system can now log events such as:

- Failed face verification.
- Duplicate attendance attempts.
- No face detected.
- Multiple faces detected.
- No enrolled users available.
- General verification errors.
- General enrollment errors.
- Wrong admin password attempts.

Security logs provide an audit trail for events that may require attention. They also make it easier to understand what happened during testing or during failed verification attempts.

---

## 6. Security Logs Dashboard

A dedicated Security Logs page was added to the Streamlit dashboard. This page allows security-related events to be reviewed and filtered.

The Security Logs page includes:

- Viewing security events in a table.
- Filtering security logs by event type.
- Searching by student ID, full name, or message.
- Filtering security logs by date range.
- Displaying security summary metrics.
- Exporting security logs as a CSV file.

This page helps separate normal attendance records from failed or suspicious events, making the system easier to monitor.

---

## 7. Admin Access Control

Basic admin access control was added to protect sensitive dashboard pages. This prevents unauthorized users from directly viewing monitoring information.

Protected pages include:

- Security Logs.
- Database Status.

When a user tries to access a protected page, the system requests an admin password. If the wrong password is entered, the system blocks access and logs the attempt as an `ACCESS_DENIED` security event.

This provides a basic access control layer for sensitive system monitoring pages.

---

## 8. Duplicate Enrollment Prevention

Enrollment validation was improved to prevent duplicate or incorrect registration attempts.

The system now blocks:

- Registering the same student ID more than once.
- Registering the same face using a different student ID.

This improves data integrity because each student ID should be linked to only one user profile, and each enrolled face should not be reused to create another identity.

Duplicate enrollment prevention also supports the security goal of the project by reducing fake or repeated registration attempts.

---

## 9. Updated Dashboard Pages

By the end of Phase 3, the Streamlit dashboard included the following main pages:

| Dashboard Page | Purpose |
|---|---|
| Register User | Enroll a user with personal information and a face image |
| Verify Attendance | Verify a user’s face and record attendance |
| View Attendance Logs | Review, filter, and export attendance records |
| Security Logs | Review, filter, and export security events |
| Database Status | View local database statistics |

The Security Logs and Database Status pages were protected using admin access control because they contain sensitive monitoring information.

---

## 10. Internal Testing

Internal testing was performed to check the main system workflows and confirm that the new reporting and security features were working correctly.

Tested workflows included:

- New student enrollment.
- Duplicate student ID prevention.
- Duplicate face prevention.
- Successful face verification.
- Unknown face rejection.
- Duplicate attendance prevention.
- Security event logging.
- Admin access control.
- Attendance filtering.
- Security log filtering.
- Attendance CSV export.
- Security logs CSV export.

The detailed testing checklist is available in:

```text
docs/phase_3_security_reporting/testing_matrix.md
```

---

## 11. Phase 3 Testing Summary

| Test Area | Expected Behavior | Status |
|---|---|---|
| New student enrollment | Valid user and face profile should be saved | Passed |
| Duplicate student ID | System should block repeated student ID registration | Passed |
| Duplicate face | System should block the same face under a different ID | Passed |
| Successful verification | Enrolled user should be recognized | Passed |
| Unknown face | Unknown user should not be accepted | Passed / needs more samples |
| Duplicate attendance | Same user should not be recorded twice on the same day | Passed |
| Failed verification logging | Failed attempts should be saved in security logs | Passed |
| Admin access control | Protected pages should require password access | Passed |
| Wrong admin password | Attempt should be logged as `ACCESS_DENIED` | Passed |
| Attendance filtering | Records should filter by search, date, and status | Passed |
| Security log filtering | Events should filter by type, search, and date | Passed |
| CSV export | Filtered records should be downloadable | Passed |

---

## 12. Privacy and Security Considerations

Phase 3 improved the security and privacy handling of the system by adding monitoring and access control features.

Security and privacy improvements included:

- Logging failed or suspicious verification attempts.
- Logging duplicate attendance attempts.
- Logging duplicate enrollment errors.
- Protecting Security Logs and Database Status pages using admin access.
- Avoiding public upload of local database files.
- Keeping biometric-related data local during development.
- Supporting CSV export only from dashboard views, not from public files.

Although these features improve monitoring and access control, the system is still a prototype. Stronger production-level security features, such as database encryption, full authentication, and advanced liveness detection, should be considered in future work.

---

## 13. Current Limitations

Although Phase 3 improved the system, some limitations remained.

| Limitation | Explanation |
|---|---|
| Basic admin password only | The system uses simple admin access control, not a full login system |
| No full anti-spoofing yet | The system does not yet include strong liveness detection |
| Limited testing sample | Testing was mainly internal and should be expanded with more users |
| Local database only | SQLite is suitable for a prototype but not for large deployment |
| No database encryption yet | Stored biometric encodings are not encrypted in the prototype |
| Threshold still needs evaluation | Recognition tolerance should be tested under different conditions |

These limitations were left for later phases, especially evaluation, optimization, and final improvement planning.

---

## 14. Phase 3 Outcome

Phase 3 successfully improved the Secure Attendance System by adding reporting, security logging, admin access control, duplicate enrollment prevention, and internal testing.

The main outcomes of Phase 3 were:

- Attendance logs became easier to search, filter, summarize, and export.
- Security-related events could be recorded and reviewed.
- A dedicated Security Logs dashboard page was added.
- Sensitive monitoring pages were protected with admin access control.
- Duplicate student ID and duplicate face enrollment were prevented.
- Internal testing confirmed that the main workflows were functioning correctly.
- The system became more prepared for evaluation and final optimization.

By the end of Phase 3, the project had moved beyond a basic MVP and became a more secure and monitorable attendance system prototype.

---

## 15. Next Steps for Phase 4

The next phase should focus on evaluation, optimization, and documenting system limitations.

Planned Phase 4 tasks include:

- Evaluate different face recognition tolerance values.
- Test the system under different lighting conditions.
- Test the system with different face poses.
- Analyze successful and failed verification cases.
- Document system limitations.
- Improve final repository organization.
- Prepare evaluation results for the final report.
- Improve the user interface where needed.
- Prepare the system for final submission and demonstration.

---