import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0

cap = cv2.VideoCapture(1)
detector = htm.handDetector()
pos = []

while True:
    success, frame = cap.read()
    frame = detector.findHands(frame)
    pos = detector.findPosition(frame)
    if len(pos) != 0:
        print(pos[4])    
    #cTime = current time, ptime = previous time    
    cTime = time.time()
    fps = 1/(cTime-pTime) 
    pTime = cTime

    cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,255,0), thickness=1)

    cv2.imshow("Image", frame)
    k = cv2.waitKey(33)
    if k == 27:
        break
