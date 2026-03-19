import cv2
import pyautogui
import base64
import numpy as np

def start_gesture(state):
    """
    Starts the gesture control module.
    Uses basic OpenCV for camera feed and simple color-based gesture detection.
    """
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        state.log.append("Error: Cannot access webcam")
        state.camera_ok = False
        return

    state.camera_ok = True
    state.log.append("Camera initialized successfully")

    screen_width, screen_height = pyautogui.size()
    prev_x, prev_y = 0, 0
    smoothing = 0.5

    # Define color range for skin detection (basic gesture detection)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    while state.running:
        ret, frame = cap.read()
        if not ret:
            state.log.append("Error: Failed to read frame from camera")
            break

        # Flip horizontally for mirror effect
        frame = cv2.flip(frame, 1)

        # Convert to HSV for skin detection
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create skin mask
        skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)

        # Find contours in the skin mask
        contours, _ = cv2.findContours(skin_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Find the largest contour (likely the hand)
            largest_contour = max(contours, key=cv2.contourArea)

            if cv2.contourArea(largest_contour) > 5000:  # Minimum area threshold
                # Get bounding rectangle
                x, y, w, h = cv2.boundingRect(largest_contour)

                # Calculate center of hand
                center_x = x + w // 2
                center_y = y + h // 2

                # Convert to screen coordinates
                screen_x = int(center_x * screen_width / frame.shape[1])
                screen_y = int(center_y * screen_height / frame.shape[0])

                # Apply smoothing
                screen_x = int(prev_x + (screen_x - prev_x) * smoothing)
                screen_y = int(prev_y + (screen_y - prev_y) * smoothing)

                # Move mouse cursor
                pyautogui.moveTo(screen_x, screen_y)
                prev_x, prev_y = screen_x, screen_y

                # Draw rectangle around detected hand
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Encode frame as base64 for web transmission
        _, buffer = cv2.imencode('.jpg', frame)
        state.camera_frame = base64.b64encode(buffer).decode('utf-8')

        # Show camera feed window
        cv2.imshow('Gesture Control (Basic)', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    state.camera_ok = False
    state.log.append("Gesture control stopped")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        state.log.append("Error: Cannot access webcam")
        state.camera_ok = False
        return

    state.camera_ok = True
    state.log.append("Camera initialized successfully")

    screen_width, screen_height = pyautogui.size()
    prev_x, prev_y = 0, 0
    smoothing = 0.5  # Smoothing factor for cursor movement
    screen_width, screen_height = pyautogui.size()
    prev_x, prev_y = 0, 0
    smoothing = 0.5  # Smoothing factor for cursor movement
    
    while state.running:
        ret, frame = cap.read()
        if not ret:
            state.log.append("Error: Failed to read frame from camera")
            break

        # Flip horizontally for mirror effect
        frame = cv2.flip(frame, 1)

        # Convert to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]

            # Get index finger tip position
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            # Convert normalized coordinates to screen coordinates
            x = int(index_finger.x * screen_width)
            y = int(index_finger.y * screen_height)

            # Apply smoothing
            x = int(prev_x + (x - prev_x) * smoothing)
            y = int(prev_y + (y - prev_y) * smoothing)

            # Move mouse cursor
            pyautogui.moveTo(x, y)
            prev_x, prev_y = x, y

            # Check for pinch gesture (left click)
            distance = np.linalg.norm(np.array([thumb.x, thumb.y]) - np.array([index_finger.x, index_finger.y]))
            if distance < 0.05:  # Threshold for pinch
                pyautogui.click()
                state.log.append("Mouse click detected")

        # Encode frame as base64 for web transmission
        _, buffer = cv2.imencode('.jpg', frame)
        state.camera_frame = base64.b64encode(buffer).decode('utf-8')

        # Show camera feed window (optional - can be commented out)
        cv2.imshow('Gesture Control', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    hands.close()
    state.camera_ok = False
    state.log.append("Gesture control stopped")