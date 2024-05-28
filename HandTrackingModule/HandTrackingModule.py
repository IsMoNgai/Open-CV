# https://developers.google.com/mediapipe/solutions/vision/hand_landmarker

import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode = False, maxHands = 2, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, frame, draw = True):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        
        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, hand, self.mpHands.HAND_CONNECTIONS)
        
        return frame

    # return a list containing all hands's position existed in frame
    def findPosition(self, frame, draw = True, color = (0, 255, 0)):

        lmList = []
        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:   
                temp = []             
                for id, lm in enumerate(hand.landmark):
                    # print(id, lm) #the  are giving ratio pos
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y*h)
                    temp.append([id, cx, cy])
                    # print(id, cx, cy)
                    if draw:
                        cv2.putText(frame, f'{int(id)}', (cx,cy), cv2.FONT_HERSHEY_PLAIN, 1, color, 1)
                lmList.append(temp)
        return lmList
    
    # This functions return a list of boolean indicating of finger is up or not for one hand
    def fingerUp(self, frame, handNo):
        lmList = self.findPosition(frame, draw = False)
        

        fingerUp = [0,0,0,0,0]
        
        if len(lmList) != 0:
            lmList = lmList[handNo]
            # thumb:
            if lmList[4][1] > lmList[17][1]: 
                thumb = lmList[4][1] > lmList[3][1]
            else:
                thumb = lmList[4][1] < lmList[3][1]

            fingerUp = [
                thumb,
                lmList[8][2] < lmList[7][2],
                lmList[12][2] < lmList[11][2],
                lmList[16][2] < lmList[15][2],
                lmList[20][2] < lmList[19][2]
            ]

        return fingerUp

    def showFps(self, frame, pTime):
        cTime = time.time()
        fps = 1/(cTime-pTime) 
        pTime = cTime

        cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,255,0), thickness=1)

        return pTime

def main():    
    # pTime = 0

    # cap = cv2.VideoCapture(0)
    # detector = handDetector()
    # pos = []

    # while True:
    #     success, frame = cap.read()
    #     frame = detector.findHands(frame, False)
    #     pos = detector.findPosition(frame)

    #     for hand in range(len(pos)):
    #         if hand == 1:
    #             print(detector.fingerUp(frame, hand))
    #     # if len(pos) != 0:
    #     #     print("start")
    #     #     print(pos)    
    #     #cTime = current time, ptime = previous time    

    #     pTime = detector.showFps(frame, pTime)

    #     cv2.imshow("Image", frame)
    #     k = cv2.waitKey(33)
    #     if k == 27:
    #         break
    pass

if __name__ == "__main__":
    main()