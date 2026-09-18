from dataclasses import dataclass
from typing import List, Optional, Tuple

import cv2

try:
    import mediapipe as mp
except ImportError:  # Allows documentation/tests to import the package without MediaPipe.
    mp = None


@dataclass
class FaceLandmarks:
    points: List[Tuple[float, float]]
    bbox: Tuple[int, int, int, int]


class FaceDetector:
    def __init__(self, max_faces: int = 2, min_detection_confidence: float = 0.5,
                 min_tracking_confidence: float = 0.5) -> None:
        if mp is None:
            raise ImportError("MediaPipe is required. Install packages from requirements.txt")
        self._mesh = mp.solutions.face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=max_faces,
            refine_landmarks=True,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
        )

    def process(self, frame) -> List[FaceLandmarks]:
        height, width = frame.shape[:2]
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self._mesh.process(rgb)
        faces: List[FaceLandmarks] = []
        if not result.multi_face_landmarks:
            return faces

        for face in result.multi_face_landmarks:
            points = [(landmark.x, landmark.y) for landmark in face.landmark]
            xs = [int(x * width) for x, _ in points]
            ys = [int(y * height) for _, y in points]
            x1, x2 = max(0, min(xs)), min(width - 1, max(xs))
            y1, y2 = max(0, min(ys)), min(height - 1, max(ys))
            faces.append(FaceLandmarks(points, (x1, y1, x2 - x1, y2 - y1)))
        return faces

    def close(self) -> None:
        self._mesh.close()


def draw_face_box(frame, face: FaceLandmarks, color=(0, 200, 0)):
    x, y, w, h = face.bbox
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
    return frame
