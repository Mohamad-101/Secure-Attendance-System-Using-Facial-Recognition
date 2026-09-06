# Threshold Testing Plan

## Project

Secure Attendance System with Face Authentication

## Phase

Phase 4: Evaluation, Optimization, and Model Refinement

## Objective

The objective of this testing plan is to evaluate how different face-recognition tolerance values affect attendance verification reliability.

The system currently uses a pretrained `dlib` / `face_recognition` model to generate 128-dimensional face encodings. The project does not train a custom ResNet model from scratch. Instead, model refinement is performed through threshold testing, distance analysis, and evaluation under different image conditions.

---

## 1. Purpose of Threshold Testing

Face recognition in this project is based on comparing a submitted face image with stored facial encodings in the local SQLite database. The comparison produces a face distance value.

A smaller face distance means the submitted face is more similar to the stored enrolled face. A larger face distance means the submitted face is less similar.

Threshold testing is important because the selected tolerance value affects whether the system accepts or rejects a face match.

The purpose of this testing plan is to:

- Test different tolerance values.
- Understand how strict or flexible each value is.
- Observe how face distance changes under different image conditions.
- Select a practical tolerance value for the attendance system.
- Document the system’s current verification behavior.

---

## 2. Current Verification Logic

During attendance verification, the system compares the submitted face image with stored facial encodings in the database.

A user is accepted if the best face distance is less than or equal to the selected tolerance value.

```text
If best_face_distance <= tolerance:
    Accept identity
Else:
    Reject identity
```

The default tolerance used by the system is:

```text
0.60
```

This value is commonly used as a practical default for the `face_recognition` library. However, it still needs to be tested because real results may change depending on lighting, pose, camera quality, and image clarity.

---

## 3. Tested Tolerance Values

The following tolerance values were selected for evaluation:

| Tolerance | Description | Expected Behavior |
|---|---|---|
| 0.45 | Very strict | More likely to reject uncertain matches |
| 0.50 | Strict | Reduces false acceptance but may reject valid users |
| 0.55 | Balanced | Middle value between strict and default |
| 0.60 | Default system setting | Practical default used during the project |
| 0.65 | More flexible | More likely to accept matches but may increase risk |

A lower tolerance value makes the system stricter. This may reduce false acceptance, but it can also increase false rejection.

A higher tolerance value makes the system more flexible. This may reduce false rejection, but it can also increase the risk of accepting incorrect matches.

---

## 4. Evaluation Method

The system was evaluated using a local threshold evaluation script.

The script compares a local test face image with the enrolled face profiles stored in the SQLite database. It calculates the best face distance and checks whether the submitted face would be accepted or rejected at each tolerance value.

The general evaluation process is:

1. Enroll a user with a clear face image.
2. Select a test face image for verification.
3. Generate a face encoding for the test image.
4. Load stored facial encodings from the local database.
5. Compare the new encoding with the stored encodings.
6. Find the closest stored profile.
7. Record the best face distance.
8. Test the result against multiple tolerance values.
9. Document whether the image is accepted or rejected.

---

## 5. Evaluation Script

The evaluation script is stored in:

```text
scripts/evaluate_thresholds.py
```

The script is used for local testing only. It helps evaluate the effect of different tolerance values without changing the main application code.

Example command:

```bash
python scripts/evaluate_thresholds.py test_images/good_lighting.jpg
```

The script should be run only with local test images. Face images and biometric data should not be uploaded to GitHub.

---

## 6. Result Recording Template

The following table format can be used to record threshold testing results.

| Test Case | Image Condition | Best Face Distance | 0.45 | 0.50 | 0.55 | 0.60 | 0.65 | Notes |
|---|---|---|---|---|---|---|---|---|
| T01 | Good lighting image |  |  |  |  |  |  |  |
| T02 | Low lighting image |  |  |  |  |  |  |  |
| T03 | Bright lighting image |  |  |  |  |  |  |  |
| T04 | Side pose image |  |  |  |  |  |  |  |


Each tolerance column should show whether the image was accepted or rejected.

Example values:

```text
Accepted
Rejected
No face detected
Not tested
```

---

## 7. Recorded Threshold Results

The following results were recorded during local evaluation using the threshold evaluation script.

| Test Case | Image Condition | Best Face Distance | 0.45 | 0.50 | 0.55 | 0.60 | 0.65 | Notes |
|---|---|---|---|---|---|---|---|---|
| T01 | Good lighting | 0.4621 | Rejected | Accepted | Accepted | Accepted | Accepted | Clear image accepted at default tolerance, but rejected by very strict tolerance |
| T02 | Low lighting | 0.5176 | Rejected | Rejected | Accepted | Accepted | Accepted | Low lighting increased the distance, but the image was accepted at 0.55 and above |
| T03 | Bright lighting | 0.4878 | Rejected | Accepted | Accepted | Accepted | Accepted | Bright lighting still allowed verification at 0.50 and above |
| T04 | Side pose | N/A | No face detected | No face detected | No face detected | No face detected | No face detected | Side pose affected face detection |

---

## 8. Interpretation of the Results

The threshold results show that the system performs best with clear and front-facing images. The good lighting image produced a face distance of `0.4621`, which was rejected by the very strict tolerance value `0.45`, but accepted by tolerance values `0.50`, `0.55`, `0.60`, and `0.65`.

The low lighting image produced a higher face distance of `0.5176`. This means that low lighting made the match less strong. The image was rejected at `0.45` and `0.50`, but accepted at `0.55`, `0.60`, and `0.65`.

The bright lighting image produced a face distance of `0.4878`. It was rejected at `0.45`, but accepted at `0.50` and above. This shows that the system can still work under brighter lighting, but very strict thresholds may reject valid users.

The side pose image could not be processed because no face was detected. This shows that the current system is sensitive to face orientation and works better with clear, frontal images.

Based on these results, the default tolerance value of `0.60` is practical for this prototype because it accepted the valid user under good, low, and bright lighting conditions. However, lower thresholds such as `0.45` and `0.50` may be too strict for realistic attendance conditions.

---

## 9. Same Image Reuse Observation

An important observation during testing is that if the exact same image used during enrollment is reused during verification, the face distance can become:

```text
0.0000
```

This is expected because the stored encoding and submitted encoding are generated from the same image.

However, this does not represent realistic attendance verification. In a real attendance scenario, the verification image should be different from the enrollment image, preferably captured live using the camera.

---

## 10. Privacy Handling

All testing was performed locally.

Privacy precautions included:

- Keeping test face images on the local machine only.
- Not uploading face images to GitHub.
- Not uploading local SQLite database files to GitHub.
- Not uploading biometric encodings or test data.
- Recording only numerical evaluation results in documentation.
- Using `.gitignore` to exclude sensitive local files.

This supports a privacy-aware evaluation process.

---

## 11. Limitations of Threshold Testing

Threshold testing is useful, but it has limitations.

| Limitation | Explanation |
|---|---|
| Small test sample | Testing was performed on a limited number of local images |
| Limited users | More enrolled users are needed for stronger evaluation |
| Image conditions vary | Lighting, pose, and camera quality affect face distance |
| No full FAR / FRR analysis | False acceptance and false rejection rates were not fully calculated |
| No liveness detection | The system does not yet verify whether the face is live |
| Pose sensitivity | Side-facing images may fail detection or increase face distance |

These limitations should be considered when interpreting the evaluation results.

---

## 12. Summary

This testing plan defines how threshold values are evaluated in the Secure Attendance System.

The system uses a pretrained `dlib` / `face_recognition` model to generate facial encodings. Verification is performed by comparing the submitted face encoding with stored encodings and checking whether the best face distance is below the selected tolerance value.

The tested tolerance values were:

```text
0.45, 0.50, 0.55, 0.60, 0.65
```

The local evaluation showed that:

- Good lighting produced a face distance of `0.4621`.
- Low lighting produced a face distance of `0.5176`.
- Bright lighting produced a face distance of `0.4878`.
- Side pose resulted in no face being detected.

The default tolerance value of `0.60` accepted the valid user under the tested good, low, and bright lighting conditions. The results also show that very strict tolerance values may reject valid users, especially when lighting conditions are not ideal.

