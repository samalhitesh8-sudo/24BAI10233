from typing import Sequence, Tuple
import cv2
import numpy as np

# Outer-lip landmarks: left, upper/lower inner points, right.
MOUTH = (61, 13, 291, 14, 82, 312)


def mouth_aspect_ratio(landmarks: Sequence[Tuple[float, float]], width: int, height: int) -> float:
    points = [np.array([landmarks[i][0] * width, landmarks[i][1] * height], dtype=np.float32) for i in MOUTH]
    left, top, right, bottom, upper_side, lower_side = points
    horizontal = np.linalg.norm(left - right)
    if horizontal == 0:
        return 0.0
    vertical_1 = np.linalg.norm(top - bottom)
    vertical_2 = np.linalg.norm(upper_side - lower_side)
    return float((vertical_1 + vertical_2) / (2.0 * horizontal))


def draw_mouth_points(frame, landmarks, width: int, height: int):
    points = [(int(landmarks[i][0] * width), int(landmarks[i][1] * height)) for i in MOUTH]
    for point in points:
        cv2.circle(frame, point, 2, (0, 100, 255), -1)
    return frame
