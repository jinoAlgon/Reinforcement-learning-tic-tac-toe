import cv2
import mediapipe as mp
import numpy as np

# def angle(a, b, c):
#     ab = np.array([a.x - b.x, a.y - b.y])
#     bc = np.array([c.x - b.x, c.y - b.y])
#     cos_angle = np.dot(ab, bc) / (np.linalg.norm(ab) * np.linalg.norm(bc))
#     return np.degrees(np.arccos(cos_angle))

def count_fingers(hand_landmarks, handedness):
    count = 0

    # Check thumb
    thumb_tip = hand_landmarks.landmark[4]
    thumb_knuckle = hand_landmarks.landmark[2]

    if handedness.classification[0].label == 'Right':
        if thumb_tip.x < thumb_knuckle.x:
            count += 1
    elif handedness.classification[0].label == 'Left':
        if thumb_tip.x > thumb_knuckle.x:
            count += 1

    # Check other fingers
    tips = [8, 12, 16, 20]  # fingertip landmark IDs
    dips = [7, 11, 15, 19]  # corresponding knuckles landmark IDs
    for tip, dip in zip(tips, dips):
        tip_y = hand_landmarks.landmark[tip].y
        dip_y = hand_landmarks.landmark[dip].y

        if tip_y < dip_y:
            count += 1

    return count

def get_finger_count():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    # Initialize MediaPipe Hands
    with mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5,
                        min_tracking_confidence=0.5) as hands:
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            ret, frame = cap.read()

            # Convert the image to RGB
            image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

            image.flags.writeable = False

            # Perform hand detection
            results = hands.process(image)

            # Draw hand landmarks
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                finger_counts = []
                for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # Count fingers for the current hand
                    fingers = count_fingers(hand_landmarks, handedness)
                    finger_counts.append(fingers)

                # Calculate the total number by adding finger counts from both hands
                total_fingers = sum(finger_counts)
                print("Total number of fingers:", total_fingers)
                cap.release()
                cv2.destroyAllWindows()
                return total_fingers

            cv2.imshow('MediaPipe Hands', image)

            if cv2.waitKey(5) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


# get_finger_count()