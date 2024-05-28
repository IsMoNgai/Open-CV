import cv2
import mediapipe as mp
import time

class FaceDetector():
    def __init__(self,min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh()
        self.drawSpec = self.mpDraw.DrawingSpec(thickness = 0.1, circle_radius = 0.1)
    
    def findFace(self, frame, draw = True):
        faces = []
        self.imgRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRgb)
        
        if self.results.multi_face_landmarks:
            for face in self.results.multi_face_landmarks:
                facel = []
                if draw:
                    self.mpDraw.draw_landmarks(frame, face)
                for id, lm in enumerate(face.landmark):
                    ih, iw, ic = frame.shape
                    x, y = int(lm.x*iw), int(lm.y*ih)
                    facel.append([x, y])
                faces.append(facel)

        return frame, faces
    
    def highlightPtr(self, frame, id, faces):
        if len(faces) != 0:
            x, y = faces[0][id][0], faces[0][id][1]
            
            cv2.circle(frame, (x,y), 5, (0,255,0), 2)
        return frame
    
    def numberPtr(self, frame, faces):
        if len(faces) != 0:
            for id in range(len(faces[0])):
               cv2.putText(frame, f'{id}', (faces[0][id][0],faces[0][id][1]), cv2.FONT_HERSHEY_PLAIN, 0.5, (0, 255, 0), 1)
        return frame


def main():
    cap = cv2.VideoCapture(0)
    cTime, pTime = 0, 0

    faceDetector = FaceDetector()

    while True:
        success, frame = cap.read()

        frame, faces = faceDetector.findFace(frame)
        # faceDetector.highlightPtr(frame, 1, faces)
        # faceDetector.numberPtr(frame, faces)
        
        # if len(faces) != 0:
        #     print(faces[0])

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(frame, f"fps: {int(fps)}", (20,40), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == 27:
            break

if __name__ == "__main__":
    main()