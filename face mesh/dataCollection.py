import cv2
import mediapipe as mp
import time
import numpy as np
import faceMesh as fm
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)

face_detector = fm.FaceDetector()
hand_detector = htm.handDetector()

offset = 20
imgSize = 300

while True:
    success, frame = cap.read()

    frame, faces = face_detector.findFace(frame)
    frame = hand_detector.findHands(frame)
    hand = hand_detector.findPosition(frame)

    if hand:
        hand = hand[0]
        print(hand[len(hand)-1])
        x, y, x_max, y_max = hand[len(hand)-1]
        imgCap = frame[y - offset:y_max + offset, x - offset:x_max + offset]
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)*255

        imgCapShape = imgCap.shape
        imgSize = imgCap.shape[0] + 100

        imgWhite[0: imgCapShape[0], 0 : imgCapShape[1]] = imgCap

        cv2.imshow("imgCap", imgCap)
        cv2.imshow("imgWhite", imgWhite)
    
    

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == 27:
        break
