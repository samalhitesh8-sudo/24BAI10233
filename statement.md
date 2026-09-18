# Project Statement: Driver Drowsiness Detection

## 1. Problem statement

Long-distance driving and lack of rest can reduce a driver's attention and reaction time. A normal webcam can be used to observe visible signs such as prolonged eye closure and repeated yawning. However, a single frame is not enough because normal blinking, speaking, or looking away can produce similar movements.

This project develops a Python-based system that checks facial landmarks over several frames and displays a warning when the measured signs indicate possible drowsiness.

## 2. Scope of the project

The project covers a local computer-vision application that:

- Accepts a webcam or recorded video as input.
- Detects one main face using MediaPipe Face Mesh.
- Calculates Eye Aspect Ratio (EAR) and Mouth Aspect Ratio (MAR).
- Uses time-based thresholds to reduce false alarms.
- Displays the current state and warning on the video.
- Optionally saves an annotated output video.
- Handles a missing face without stopping the program.

It works best with one visible face in ordinary indoor or daylight conditions.


## 3. High-level features

1. **Face landmark detection:** Finds facial points from each readable frame.
2. **Eye monitoring:** Uses EAR to estimate whether the eyes remain closed.
3. **Yawn estimation:** Uses MAR to estimate increased mouth opening.
4. **Temporal decision logic:** Checks several frames before producing a warning.
5. **System states:** Displays `ALERT`, `ATTENTION`, or `DROWSY`.
6. **Visual feedback:** Shows the face box, eye and mouth points, EAR, MAR, and status message.
7. **Alert output:** Displays a warning and can produce a short beep.
8. **Video support:** Reads from a webcam or video file and can save an annotated video.
9. **Safe missing-face handling:** Shows `No face detected` and continues processing.

## 4. Expected outcome

The completed system should remain in the ALERT state during normal open-eye frames, show ATTENTION during a possible yawn condition, and show DROWSY after sustained low-EAR input in a controlled test. The decision logic should also continue safely when the face is temporarily not visible.
