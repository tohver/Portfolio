import os
import cv2
import time
import numpy as np
import handTracking as ht
import math

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
previousTime = 0
 
detector = ht.handDetector(detectionConfidence=0.7)
 
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    landmarkList = detector.findPosition(img, draw=False)
    if len(landmarkList) != 0:
 
        thumbX, thumbY = landmarkList[4][1], landmarkList[4][2]
        indexFingerX, indexFingerY = landmarkList[8][1], landmarkList[8][2]
        cx, cy = (thumbX + indexFingerX) // 2, (thumbY + indexFingerY) // 2

        middleX, middleY = landmarkList[12][1], landmarkList[12][2]
        indexDipX, indexDipY = landmarkList[7][1], landmarkList[7][2]


        cv2.circle(img, (thumbX, thumbY), 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (indexFingerX, indexFingerY), 5, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (thumbX, thumbY), (indexFingerX, indexFingerY), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
 
        length = math.hypot(indexFingerX - thumbX, indexFingerY - thumbY)
        f_power = math.hypot(middleX-indexDipX, middleY-indexDipY)
        
        if length > 50:
            cv2.circle(img, (cx, cy), 4, (0, 255, 0), cv2.FILLED)
            os.system("start \"\" https://soundcloud.com/you/library")
            time.sleep(3)
        if f_power > 25:
            cv2.putText(img, 'You are rude', (wCam//2, hCam//2), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,255,255), 3)

    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 200, 128), 3)
 
    cv2.imshow("Img", img)
    if cv2.waitKey(5) & 0xFF == 27:
        break

