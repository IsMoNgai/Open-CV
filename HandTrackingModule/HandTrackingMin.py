# https://developers.google.com/mediapipe/solutions/vision/hand_landmarker

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, frame = cap.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            for id, lm in enumerate(hand.landmark):
                # print(id, lm) #the  are giving ratio pos
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y*h)
                print(id, cx,cy)
                if id == 8:
                    cv2.circle(frame, (cx,cy), 25, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(frame, hand, mpHands.HAND_CONNECTIONS)

    #cTime = current time, ptime = previous time
    cTime = time.time()
    fps = 1/(cTime-pTime) 
    pTime = cTime

    cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,255,0), thickness=1)

    cv2.imshow("Image", frame)
    k = cv2.waitKey(33)
    if k == 27:
        break