import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
import numpy as np

class handPainter(htm.handDetector):

    def __init__(self, mode = False, maxHands = 2, detectionCon = 0.5, trackCon = 0.5):
        super().__init__(mode, maxHands, detectionCon, trackCon)

    def paint(self, inputPin, fps = True, stopKey = 27):

        pTime = 0
        pos = []
        px, py = 0, 0
        color = (255, 255, 255)
        eraser = False


        cap = cv2.VideoCapture(inputPin)
        success, oframe = cap.read()
        paintBoard = np.zeros(oframe.shape, np.uint8)
        

        while True:
            success, oframe = cap.read()

            oframe = self.findHands(oframe, False)
            frame = oframe.copy()

            if fps: pTime = self.showFps(frame, pTime)

            pos = self.findPosition(frame, False)
            finger = self.fingerUp(frame, 0)

            if len(pos) != 0:
                pos = pos[0]
                x, y = pos[8][1], pos[8][2]
                if not eraser:
                    cv2.circle(frame, (x,y), 5, color, cv2.FILLED)

                if finger == [True for _ in range(5)]:
                    paintBoard = np.zeros(frame.shape, np.uint8)

                elif finger[1] and finger[2]:
                    # selection mode
                    if x >= frame.shape[1]-100 and y <= 50:
                        cv2.rectangle(frame, (frame.shape[1]-100, 0), (frame.shape[1], 50), (255, 0, 0), cv2.FILLED)
                        color = (255, 0, 0)
                        eraser = False
                    else: 
                        cv2.rectangle(frame, (frame.shape[1]-100, 0), (frame.shape[1], 50), (155, 0, 0), cv2.FILLED)
                    if (x >= frame.shape[1]-100 and x <= frame.shape[1]) and (y <= 150 and y >= 100):
                        cv2.rectangle(frame, (frame.shape[1]-100, 100), (frame.shape[1], 150), (0, 255, 0), cv2.FILLED)
                        color = (0, 255, 0)
                        eraser = False
                    else: 
                        cv2.rectangle(frame, (frame.shape[1]-100, 100), (frame.shape[1], 150), (0, 155, 0), cv2.FILLED)
                    if (x >= frame.shape[1]-100 and x <= frame.shape[1]) and (y <= 250 and y >= 200):
                        cv2.rectangle(frame, (frame.shape[1]-100, 200), (frame.shape[1], 250), (0, 0, 255), cv2.FILLED)
                        color = (0, 0, 255)
                        eraser = False
                    else: 
                        cv2.rectangle(frame, (frame.shape[1]-100, 200), (frame.shape[1], 250), (0, 0, 155), cv2.FILLED)
                    if (x >= frame.shape[1]-100 and x <= frame.shape[1]) and (y <= 350 and y >= 300):
                        cv2.rectangle(frame, (frame.shape[1]-100, 350), (frame.shape[1], 300), (255, 255, 255), cv2.FILLED)
                        cv2.putText(frame, "eraser", (frame.shape[1]-100, 350), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)
                        color = (0, 0, 0)
                        eraser = False
                    else:
                        cv2.rectangle(frame, (frame.shape[1]-100, 350), (frame.shape[1], 300), (255, 255, 255), cv2.FILLED)
                        cv2.putText(frame, "eraser", (frame.shape[1]-100, 350), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

                elif finger[1]:
                    # paint mode
                    if (px == 0 and py == 0) or (abs(px - x) > 30 or abs(py-y) > 30):
                        px, py = x, y

                    # cv2.line(paintBoard, (x,y), (x+10,y+10), self.color, 50, cv2.FILLED) 
                    if not eraser:
                        cv2.line(paintBoard, (px,py), (x, y), color, 5)
                        px, py = x, y
                    

            
            imgInv = cv2.cvtColor(paintBoard, cv2.COLOR_BGR2GRAY)
            _, imgInv = cv2.threshold(imgInv, 25, 255, cv2.THRESH_BINARY_INV)
            imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)

            frame = cv2.bitwise_and(frame, imgInv)
            frame = cv2.bitwise_or(frame, paintBoard)
            
            cv2.imshow("Image", frame)
            
            k = cv2.waitKey(1)
            if k == stopKey:
                break
    
def main():
    detector = handPainter()
    detector.paint(0)

if __name__ == '__main__':
    main()