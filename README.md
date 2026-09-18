# Driver Drowsiness Detection

## 1. Project overview

Driver Drowsiness Detection is a Python computer-vision project for identifying possible driver drowsiness from a webcam or recorded video. It uses facial landmarks to calculate eye and mouth measurements and displays a warning when the signs continue over several frames.

## 2. Features

- Detects facial landmarks using MediaPipe Face Mesh.
- Calculates Eye Aspect Ratio (EAR) for eye-closure detection.
- Calculates Mouth Aspect Ratio (MAR) for possible yawn detection.
- Uses temporal thresholds to reduce false alarms from normal blinking.
- Displays `ALERT`, `ATTENTION`, or `DROWSY` states.
- Shows EAR, MAR, face box, and landmark points on the video.
- Gives a warning when the drowsiness condition is reached.
- Handles frames with no detected face without crashing.
- Supports webcam input, video-file input, and optional output-video saving.

## 3. Technologies and tools used

- **Python 3.9+** — main programming language.
- **OpenCV** — video capture, display, drawing, and video writing.
- **MediaPipe Face Mesh** — facial-landmark detection.
- **NumPy** — coordinate and distance calculations.
- **Pytest** — unit testing.
- **Visual Studio Code** — development and testing environment.
- **Mermaid** — architecture and design diagrams.

## 4. Project structure

```text
Driver-Drowsiness-Detection/
├── README.md
├── statement.md
├── requirements.txt
├── src/
│   ├── main.py
│   ├── face_detection.py
│   ├── eye_detection.py
│   ├── yawn_detection.py
│   ├── drowsiness.py
│   └── alert.py
├── assets/                    # Design diagrams
├── results/                   # Sample output screenshots
│   ├── ALERT.png
│   ├── ATTENTION.png
│   ├── DROWSY.png
│   └── NO FACE DETECTED.png
└── tests/
    ├── test_drowsiness.py
    └── smoke_test.py
```

## 5. Installation

Use Python 3.9 or newer. Open a terminal in the project folder and run:

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows
.venv\\Scripts\\activate

# Linux/macOS
source .venv/bin/activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

If MediaPipe installation fails, try a Python version supported by the installed MediaPipe release.

## 6. How to run

Run the system using the default webcam:

```bash
python src/main.py
```

Press **q** in the preview window to stop the program.

Run the system using a video file and save the annotated result:

```bash
python src/main.py --source data/sample.mp4 --output results/drowsiness_output.mp4
```

For a computer without a display:

```bash
python src/main.py --source data/sample.mp4 --output results/output.mp4 --no-display
```

## 7. Testing instructions

Run the unit tests using Pytest:

```bash
pytest -q
```

A camera-independent smoke test is also available:

```bash
python tests/smoke_test.py
```

The tests check the decision logic for normal alertness, sustained eye closure, and repeated mouth opening. For a complete evaluation, use consented videos from several people and record false alarms, missed warnings, detection rate, and warning delay.

## 8. Screenshots and sample results

Sample output screenshots are available in the `results/` folder:

- `ALERT.png` — normal open-eye condition.
- `ATTENTION.png` — attention or possible yawn condition.
- `DROWSY.png` — prolonged eye closure with a warning.
- `NO FACE DETECTED.png` — safe handling when a face is not visible.

The screenshots show the live state, EAR and MAR values, face bounding box, and facial landmark points.

## 9. Limitations

The prototype works best when one main face is visible in ordinary indoor or daylight conditions. Thresholds can change with lighting, camera position, glasses, face shape, and frame rate. The system does not identify the driver, detect phone use, understand road conditions, or guarantee that a yawn means sleepiness.

## References

[1]: https://chuoling.github.io/mediapipe/solutions/face_mesh.html "MediaPipe Face Mesh documentation"

[2]: https://docs.opencv.org/4.x/ "OpenCV documentation"

[3]: https://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf "Real-Time Eye Blink Detection using Facial Landmarks"