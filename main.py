import cv2
import mediapipe as mp
import time
import math
import controller as cnt  # Import the controller module

# Initialize Mediapipe Hand Tracking
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

# Initialize camera
cap = cv2.VideoCapture(0)
time.sleep(2)  # Delay to stabilize the script

# LED state variables
led_intensity = 0
led_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror the frame
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get hand centroid (average of landmark positions)
            x_vals = [lm.x for lm in hand_landmarks.landmark]
            y_vals = [lm.y for lm in hand_landmarks.landmark]
            centroid_x = sum(x_vals) / len(x_vals)
            centroid_y = sum(y_vals) / len(y_vals)

            # Determine if left or right hand
            if centroid_x < 0.5:  # Left side -> Control intensity
                dist = math.dist(
                    (hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y),
                    (hand_landmarks.landmark[4].x, hand_landmarks.landmark[4].y)
                )
                led_intensity = min(1, max(0, dist * 5))  # Scale and limit
                cnt.leds(led_count, led_intensity)

            else:  # Right side -> Control LED count
                fingers_up = sum(1 for i in [8, 12, 16, 20] if hand_landmarks.landmark[i].y < hand_landmarks.landmark[i - 2].y)
                led_count = min(5, max(0, fingers_up))
                cnt.leds(led_count, led_intensity)

    cv2.putText(frame, f'LEDs: {led_count}  Intensity: {led_intensity:.2f}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Palm Detect", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
