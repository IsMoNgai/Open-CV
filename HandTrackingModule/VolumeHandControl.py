import cv2
import time
import numpy as np
import HandTrackingModule as htm

##########################################

wCam, hCam = 320, 320
pTime = 0

##########################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionCon = 0.7)

while True:

    success, frame = cap.read()

    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw = False)
    
    # we need to get distance from ptr 4 to ptr 8
    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        
        rx1, ry1 = lmList[0][1], lmList[0][2]
        rx2, ry2 = lmList[5][1], lmList[5][2]
        midx, midy = (x1+x2)//2, (y1+y2)//2

        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
        cv2.circle(frame, (midx, midy), 5, (0, 0, 255), 5, cv2.FILLED)

        # print("gg", [x1,y1], [x2, y2], [int((x1+x2)/2), int((y1+y2)/2)])

        d1 = (rx1-rx2)*(rx1-rx2)+(ry1-ry2)*(ry1-ry2)
        d2 = (midx-x2)*(midx-x2)+(midy-y2)*(midy-y2)

        #   (608130/5668)
        
        # min_r = 50
        # max_r = 6000

        print([d1, d2])

        # if abs(x1-x2) < 20 and abs(y1-y2) < 20:
        #     print("zero")

    # scale this distance from 0 to 100 as conversion to volume



    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(frame, f'fps: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == 27:
        break