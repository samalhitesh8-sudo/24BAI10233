from typing import Sequence, Tuple
import cv2
import numpy as np

# MediaPipe Face Mesh landmark indices for refined eye contours.
LEFT_EYE = (33, 160, 158, 133, 153, 144)
RIGHT_EYE = (362, 385, 387, 263, 373, 380)


def _point(landmarks: Sequence[Tuple[float, float]], index: int, width: int, height: int):
    x, y = landmarks[index]
    return np.array([x * width, y * height], dtype=np.float32)


def eye_aspect_ratio(landmarks, eye_indices, width: int, height: int) -> float:
    p1, p2, p3, p4, p5, p6 = [_point(landmarks, i, width, height) for i in eye_indices]
    horizontal = np.linalg.norm(p1 - p4)
    if horizontal == 0:
        return 0.0
    return float((np.linalg.norm(p2 - p6) + np.linalg.norm(p3 - p5)) / (2.0 * horizontal))


def calculate_ear(landmarks, width: int, height: int) -> Tuple[float, float, float]:
    left = eye_aspect_ratio(landmarks, LEFT_EYE, width, height)
    right = eye_aspect_ratio(landmarks, RIGHT_EYE, width, height)
    return left, right, (left + right) / 2.0


def draw_eye_points(frame, landmarks, width: int, height: int):
    for eye in (LEFT_EYE, RIGHT_EYE):
        points = [(int(landmarks[i][0] * width), int(landmarks[i][1] * height)) for i in eye]
        cv2.polylines(frame, [np.array(points)], True, (255, 180, 0), 1)
    return frame
