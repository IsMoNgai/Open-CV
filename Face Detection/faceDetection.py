import cv2
import mediapipe as mp
import numpy
import time

cap = cv2.VideoCapture(0)
cTime, pTime = 0, 0

mpFaceDetection = mp.solutions.face_detection
mpDrawing = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

while True:
    success, frame = cap.read()

    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    
    if results.detections:
        for id, detection in enumerate(results.detections):
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = frame.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(frame, bbox, (255, 0, 255), 2)
            cv2.putText(frame, f'{int(detection.score[id]*100)}%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
            cv2.putText(frame, f'identity: {id}', (bbox[0], bbox[1]-40), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
            # print(results.detections)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(frame, f'fps {int(fps)}', (20, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 0), 2)

    cv2.imshow("frame", frame)
    
    if cv2.waitKey(1) == 27: #lower waitKey increase fps
        break