import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from drowsiness import DrowsinessMonitor


def test_alert_status_for_normal_measurements():
    monitor = DrowsinessMonitor()
    status = monitor.update(0.32, 0.25)
    assert status.state == "ALERT"


def test_eye_closure_event_becomes_drowsy():
    monitor = DrowsinessMonitor(closed_frames=3, yawn_frames=50, history_size=1)
    for _ in range(3):
        status = monitor.update(0.12, 0.2)
    assert status.state == "DROWSY"


def test_yawn_event_gives_attention():
    monitor = DrowsinessMonitor(closed_frames=50, yawn_frames=3, history_size=1)
    for _ in range(3):
        status = monitor.update(0.32, 0.9)
    assert status.state == "ATTENTION"
