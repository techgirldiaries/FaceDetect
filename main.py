import argparse
import sys
import time
import cv2
from capture import CaptureManager
from consent import ensure_consent
from detect import create_detector, draw_detections
from dnn_face_detect import create_dnn_detector
from privacy import apply_privacy_mode


def parse_args():
    parser = argparse.ArgumentParser(description="Real-time webcam face detection")
    parser.add_argument("--camera", type=int, default=0, help="Camera index")
    parser.add_argument("--model", type=str, default="haar", choices=["haar", "dnn"], help="Detector model")
    parser.add_argument("--scale-factor", type=float, default=1.3, help="Haar detect scaleFactor")
    parser.add_argument("--min-neighbors", type=int, default=5, help="Haar detect minNeighbors")
    parser.add_argument("--min-size", type=int, default=30, help="Minimum face size in pixels")
    parser.add_argument("--dnn-model-path", type=str, default=None, help="Path to DNN model weights")
    parser.add_argument("--dnn-config-path", type=str, default=None, help="Path to DNN model config")
    parser.add_argument("--dnn-confidence", type=float, default=0.6, help="Minimum DNN confidence")
    parser.add_argument("--box-thickness", type=int, default=2, help="Bounding box thickness")
    parser.add_argument("--window-name", type=str, default="Video Face Detection", help="OpenCV window title")
    parser.add_argument(
        "--read-fail-sleep-ms",
        type=float,
        default=10.0,
        help="Delay in milliseconds before retrying after camera read failure",
    )
    parser.add_argument(
        "--privacy-mode",
        type=str,
        default="none",
        choices=["none", "blur", "pixelate"],
        help="Privacy mode for face anonymisation",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # Check camera consent before proceeding
    if not ensure_consent():
        print("Camera consent required to run FaceDetect.")
        sys.exit(1)

    detector = create_dnn_detector(
        model_name=args.model,
        dnn_model_path=args.dnn_model_path,
        dnn_config_path=args.dnn_config_path,
        dnn_confidence=args.dnn_confidence,
    )
    if detector is None:
        detector = create_detector(
            model_name=args.model,
            scale_factor=args.scale_factor,
            min_neighbors=args.min_neighbors,
            min_size=(args.min_size, args.min_size),
        )

    capture = cv2.VideoCapture(args.camera)
    if not capture.isOpened():
        raise RuntimeError(f"Unable to open camera index: {args.camera}")

    previous_time = time.perf_counter()
    box_colour = (255, 0, 0)
    cv2.namedWindow(args.window_name, cv2.WINDOW_AUTOSIZE)

    # Initialise capture manager and privacy mode
    capture_manager = CaptureManager()
    privacy_mode = args.privacy_mode
    frame_height, frame_width = None, None
    frame = None

    try:
        while True:
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            elif key == ord("c"):
                # Capture photo
                if frame is not None:
                    capture_manager.capture_photo(frame)
            elif key == ord("r"):
                # Toggle recording
                if not capture_manager.is_recording:
                    if frame_height and frame_width:
                        capture_manager.start_recording(frame_width, frame_height)
                else:
                    capture_manager.stop_recording()
            elif key == ord("p"):
                # Toggle privacy mode
                if privacy_mode == "none":
                    privacy_mode = "blur"
                    print("Privacy mode: blur")
                elif privacy_mode == "blur":
                    privacy_mode = "pixelate"
                    print("Privacy mode: pixelate")
                else:
                    privacy_mode = "none"
                    print("Privacy mode: off")

            if cv2.getWindowProperty(args.window_name, cv2.WND_PROP_VISIBLE) < 1:
                break

            ret, frame = capture.read()
            if not ret or frame is None:
                sleep_seconds = max(0.0, args.read_fail_sleep_ms) / 1000.0
                time.sleep(sleep_seconds)
                continue

            # Capture frame dimensions for recording
            if frame_height is None:
                frame_height, frame_width = frame.shape[:2]

            faces = detector.detect(frame)

            # Apply privacy mode before drawing boxes
            if privacy_mode != "none":
                frame = apply_privacy_mode(frame, faces, privacy_mode)

            frame = draw_detections(frame, faces, box_colour, args.box_thickness)

            # Write frame to recording if active
            if capture_manager.is_recording:
                capture_manager.write_frame(frame)

            current_time = time.perf_counter()
            elapsed = current_time - previous_time
            fps = 1.0 / elapsed if elapsed > 0 else 0.0
            previous_time = current_time

            cv2.putText(
                frame,
                f"Faces: {len(faces)}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2,
            )
            cv2.putText(
                frame,
                f"FPS: {fps:.1f}",
                (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2,
            )

            # Display recording status
            if capture_manager.is_recording:
                cv2.putText(
                    frame,
                    "REC \u25CF",
                    (10, 90),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    2,
                )

            # Display privacy mode
            if privacy_mode != "none":
                cv2.putText(
                    frame,
                    f"Privacy: {privacy_mode}",
                    (10, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 0),
                    2,
                )

            cv2.imshow(args.window_name, frame)
    finally:
        capture_manager.cleanup()
        capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()