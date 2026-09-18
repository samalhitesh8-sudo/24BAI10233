import argparse
import cv2

from face_detection import FaceDetector, draw_face_box
from eye_detection import calculate_ear, draw_eye_points
from yawn_detection import mouth_aspect_ratio, draw_mouth_points
from drowsiness import DrowsinessMonitor
from alert import AlertManager, draw_status


def run(source=0, output=None, show=True):
    capture = cv2.VideoCapture(source)
    if not capture.isOpened():
        raise RuntimeError(f"Could not open video source: {source}")
    writer = None
    detector = FaceDetector(max_faces=1)
    monitor = DrowsinessMonitor()
    alerts = AlertManager()
    try:
        while True:
            ok, frame = capture.read()
            if not ok:
                break
            height, width = frame.shape[:2]
            if output and writer is None:
                fps = capture.get(cv2.CAP_PROP_FPS) or 20.0
                writer = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

            faces = detector.process(frame)
            if faces:
                face = faces[0]
                draw_face_box(frame, face)
                left, right, ear = calculate_ear(face.points, width, height)
                mar = mouth_aspect_ratio(face.points, width, height)
                draw_eye_points(frame, face.points, width, height)
                draw_mouth_points(frame, face.points, width, height)
                status = monitor.update(ear, mar)
                draw_status(frame, status.state, ear, mar, status.message)
                if status.state == "DROWSY":
                    alerts.trigger(frame, status.message)
            else:
                cv2.putText(frame, "No face detected", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 165, 255), 2)

            if writer:
                writer.write(frame)
            if show:
                cv2.imshow("Driver Drowsiness Detection", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
    finally:
        capture.release()
        if writer:
            writer.release()
        detector.close()
        cv2.destroyAllWindows()


def main():
    parser = argparse.ArgumentParser(description="EAR/MAR based driver drowsiness detector")
    parser.add_argument("--source", default="0", help="Camera index (0) or path to a video file")
    parser.add_argument("--output", help="Optional output video path")
    parser.add_argument("--no-display", action="store_true", help="Process without opening a preview window")
    args = parser.parse_args()
    source = int(args.source) if str(args.source).isdigit() else args.source
    run(source, args.output, show=not args.no_display)


if __name__ == "__main__":
    main()
