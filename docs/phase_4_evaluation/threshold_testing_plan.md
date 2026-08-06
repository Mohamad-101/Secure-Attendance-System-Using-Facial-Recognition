# Threshold Testing Plan

## Project
Secure Attendance System with Face Authentication

## Phase
Phase 4: Evaluation, Optimization, and Model Refinement

## Objective
The objective of this testing plan is to evaluate how different face-recognition tolerance values affect attendance verification reliability.

The system currently uses a pretrained dlib/face_recognition model to generate 128-dimensional face encodings. The project does not train a custom ResNet model from scratch. Instead, model refinement is performed through threshold testing, distance analysis, and evaluation under different image conditions.

## Current Verification Logic
During attendance verification, the system compares the submitted face image with stored facial encodings in the database.

A user is accepted if the best face distance is less than or equal to the selected tolerance value.

Default tolerance:

```text
0.60