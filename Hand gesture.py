import cv2
import mediapipe as mp
import pyautogui
import time
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.6
)
mp_draw = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Gesture tracking
prev_gesture = None
last_action_time = 0
gesture_delay = 0.8

# FPS tracking
start_time = time.time()
frame_count = 0

screen_w, screen_h = pyautogui.size()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    current_gesture = None

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm = hand_landmarks.landmark

            # Get coordinates
            index_finger_tip = lm[8]
            thumb_tip = lm[4]
            index_finger_base = lm[5]

            # Check fingers
            index_up = index_finger_tip.y < lm[6].y
            middle_up = lm[12].y < lm[10].y
            ring_up = lm[16].y < lm[14].y
            pinky_up = lm[20].y < lm[18].y

            # Finger open count
            open_fingers = sum([index_up, middle_up, ring_up, pinky_up])

            # Get pixel coordinates
            ix, iy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

            # Click gesture: thumb and index close together
            thumb_index_dist = math.hypot(
                (index_finger_tip.x - thumb_tip.x) * w,
                (index_finger_tip.y - thumb_tip.y) * h
            )
            if thumb_index_dist < 30:
                current_gesture = "click"
                pyautogui.click()
                print("Gesture: click")
                time.sleep(0.3)  # to avoid multiple clicks

            # Move gesture: only index up
            elif open_fingers == 1 and index_up:
                current_gesture = "move"
                screen_x = int(index_finger_tip.x * screen_w)
                screen_y = int(index_finger_tip.y * screen_h)
                pyautogui.moveTo(screen_x, screen_y)
                print("Gesture: move")

            # Other gestures for keypress
            elif open_fingers == 1 and index_up:
                current_gesture = "up"
            elif open_fingers == 0:
                current_gesture = "down"
            elif open_fingers == 4:
                current_gesture = "right"
            elif open_fingers == 2 and index_up and middle_up:
                current_gesture = "left"

            # Trigger keypress only if gesture changed
            if current_gesture != prev_gesture and time.time() - last_action_time > gesture_delay:
                if current_gesture in ["up", "down", "left", "right"]:
                    pyautogui.press(current_gesture)
                    print(f"Gesture: {current_gesture}")
                    prev_gesture = current_gesture
                    last_action_time = time.time()

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Show FPS
    frame_count += 1
    if frame_count >= 10:
        fps = frame_count / (time.time() - start_time)
        print("FPS:", round(fps, 2))
        frame_count = 0
        start_time = time.time()

    cv2.imshow("Hand Gesture Control", frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
