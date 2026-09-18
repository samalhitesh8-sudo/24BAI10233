import time
import cv2

class AlertManager:
    def __init__(self, cooldown_seconds: float = 2.0, enable_sound: bool = True) -> None:
        self.cooldown_seconds = cooldown_seconds
        self.enable_sound = enable_sound
        self.last_alert = 0.0

    def trigger(self, frame, message: str):
        now = time.monotonic()
        if now - self.last_alert >= self.cooldown_seconds:
            if self.enable_sound:
                try:
                    print("\\a", end="", flush=True)
                except Exception:
                    pass
            self.last_alert = now
        cv2.rectangle(frame, (0, 0), (frame.shape[1], 55), (0, 0, 180), -1)
        cv2.putText(frame, message, (20, 37), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (255, 255, 255), 2, cv2.LINE_AA)
        return frame


def draw_status(frame, state: str, ear: float, mar: float, message: str):
    color = (0, 200, 0) if state == "ALERT" else (0, 180, 255) if state == "ATTENTION" else (0, 0, 255)
    cv2.putText(frame, f"State: {state}", (20, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)
    cv2.putText(frame, f"EAR: {ear:.2f}  MAR: {mar:.2f}", (20, 115), cv2.FONT_HERSHEY_SIMPLEX, 0.62, (255, 255, 255), 2)
    cv2.putText(frame, message, (20, 145), cv2.FONT_HERSHEY_SIMPLEX, 0.58, (255, 255, 255), 1)
    return frame
