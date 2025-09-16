#A test script to verify pose and camera works.

import os

import cv2  # OpenCV: used for camera input, image processing, and display
import mediapipe as mp  # MediaPipe: gives us BlazePose model and drawing utilities
from absl import logging as absl_logging

absl_logging.set_verbosity(absl_logging.ERROR)
# Suppress noisy Mediapipe/absl log messages (keeps console cleaner)

# Aliases for easier access
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils


def main():
    # Open webcam (index 0 = default camera)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open camera 0")
        return

    try:
        # Create a Pose object (BlazePose under the hood)
        # Parameters:
        # - static_image_mode=False: expects video stream, not still images
        # - model_complexity=0: lightweight version (faster, less accurate)
        # - enable_segmentation=False: we don’t need body segmentation
        # - min_detection_confidence=0.5: minimum score to accept detection
        # - min_tracking_confidence=0.5: minimum score to keep tracking once detected
        with mp_pose.Pose(
                static_image_mode=False,
                model_complexity=0,
                enable_segmentation=False,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5
        ) as pose:

            while True:
                # Capture one frame from webcam
                ok, frame = cap.read()
                if not ok:
                    continue  # skip if no frame

                # Convert frame from BGR (OpenCV default) → RGB (required by Mediapipe)
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Run pose estimation on the RGB frame
                res = pose.process(rgb)

                # If pose landmarks detected → draw skeleton on frame
                if res.pose_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,
                        res.pose_landmarks,
                        mp_pose.POSE_CONNECTIONS  # lines connecting keypoints
                    )

                # Show the result in a window
                cv2.imshow("BlazePose verify", frame)

                # Listen for keys: ESC (27) or 'q' to quit
                key = cv2.waitKey(1) & 0xFF
                if key in (27, ord('q')):
                    break

    except KeyboardInterrupt:
        # Handles Ctrl+C or PyCharm stop button gracefully
        pass

    finally:
        # Always release camera + close windows, even if an error happens
        cap.release()
        cv2.destroyAllWindows()


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
