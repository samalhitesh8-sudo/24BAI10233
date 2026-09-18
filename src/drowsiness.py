from dataclasses import dataclass
from collections import deque


@dataclass
class DrowsinessStatus:
    state: str
    score: int
    eye_closed_frames: int
    yawn_frames: int
    message: str


class DrowsinessMonitor:

    def __init__(self, ear_threshold: float = 0.21, closed_frames: int = 18,
                 mar_threshold: float = 0.65, yawn_frames: int = 12,
                 history_size: int = 5) -> None:
        self.ear_threshold = ear_threshold
        self.closed_frames_required = closed_frames
        self.mar_threshold = mar_threshold
        self.yawn_frames_required = yawn_frames
        self.ear_history = deque(maxlen=history_size)
        self.mar_history = deque(maxlen=history_size)
        self.closed_frames = 0
        self.yawn_frames = 0

    def update(self, ear: float, mar: float) -> DrowsinessStatus:
        self.ear_history.append(ear)
        self.mar_history.append(mar)
        smooth_ear = sum(self.ear_history) / len(self.ear_history)
        smooth_mar = sum(self.mar_history) / len(self.mar_history)

        if smooth_ear < self.ear_threshold:
            self.closed_frames += 1
        else:
            self.closed_frames = max(0, self.closed_frames - 2)
        if smooth_mar > self.mar_threshold:
            self.yawn_frames += 1
        else:
            self.yawn_frames = max(0, self.yawn_frames - 1)

        eye_alert = self.closed_frames >= self.closed_frames_required
        yawn_alert = self.yawn_frames >= self.yawn_frames_required
        score = int(eye_alert) * 2 + int(yawn_alert)
        if score >= 2:
            state, message = "DROWSY", "WARNING: Please take a break"
        elif score == 1:
            state, message = "ATTENTION", "Keep your eyes on the road"
        else:
            state, message = "ALERT", "Driver is alert"
        return DrowsinessStatus(state, score, self.closed_frames, self.yawn_frames, message)

    def reset(self) -> None:
        self.ear_history.clear()
        self.mar_history.clear()
        self.closed_frames = 0
        self.yawn_frames = 0
