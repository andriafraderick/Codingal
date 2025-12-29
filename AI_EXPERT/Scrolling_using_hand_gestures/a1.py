import cv2
import time
import pyautogui
import mediapipe as mp

# -----------------------------
# MediaPipe Hand Setup
# -----------------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)
mp_drawing = mp.solutions.drawing_utils

# -----------------------------
# Configuration
# -----------------------------
SCROLL_SPEED = 300        # Scroll amount
SCROLL_DELAY = 1          # Seconds between scrolls
CAM_WIDTH, CAM_HEIGHT = 640, 480

# -----------------------------
# Gesture Detection Function
# -----------------------------
def detect_gesture(hand_landmarks, handedness):
    """
    Detects scroll gestures based on finger positions.
    Returns:
        'scroll_up'    -> Open palm (5 fingers)
        'scroll_down'  -> Closed fist (0 fingers)
        'none'         -> Any other gesture
    """
    fingers = []

    # Finger tip landmarks (excluding thumb)
    finger_tips = [
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]

    # Check if fingers are raised
    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    # Thumb logic (different for left & right hand)
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]

    if (handedness == "Right" and thumb_tip.x > thumb_ip.x) or \
       (handedness == "Left" and thumb_tip.x < thumb_ip.x):
        fingers.append(1)
    else:
        fingers.append(0)

    total_fingers = sum(fingers)

    if total_fingers == 5:
        return "scroll_up"
    elif total_fingers == 0:
        return "scroll_down"
    else:
        return "none"

# -----------------------------
# Webcam Setup
# -----------------------------
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_HEIGHT)

last_scroll = 0
prev_time = 0

print("""
Gesture Scroll Control Active
-----------------------------
Open Palm  → Scroll Up
Closed Fist → Scroll Down
Press 'q' to exit
""")

# -----------------------------
# Main Loop
# -----------------------------
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Mirror the image
    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    gesture = "none"
    hand_label = "Unknown"

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, hand_info in zip(
            results.multi_hand_landmarks,
            results.multi_handedness
        ):
            hand_label = hand_info.classification[0].label
            gesture = detect_gesture(hand_landmarks, hand_label)

            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Scroll with delay
            if time.time() - last_scroll > SCROLL_DELAY:
                if gesture == "scroll_up":
                    pyautogui.scroll(SCROLL_SPEED)
                    last_scroll = time.time()
                elif gesture == "scroll_down":
                    pyautogui.scroll(-SCROLL_SPEED)
                    last_scroll = time.time()

    # FPS calculation
    curr_time = time.time()
    fps = int(1 / (curr_time - prev_time)) if prev_time else 0
    prev_time = curr_time

    # Display text
    cv2.putText(
        frame,
        f"FPS: {fps} | Hand: {hand_label} | Gesture: {gesture}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 0),
        2
    )

    cv2.imshow("Gesture Scroll Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -----------------------------
# Cleanup
# -----------------------------
cap.release()
cv2.destroyAllWindows()
