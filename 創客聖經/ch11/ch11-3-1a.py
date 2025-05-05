from cvzone.PoseModule import PoseDetector
from Pose3D import plotPose3D
import cv2

detector = PoseDetector()

img = cv2.imread("images/pose.jpg")
img = detector.findPose(img)
lmList, bboxInfo = detector.findPosition(img, draw=False, bboxWithHands=False)
if lmList:
    print("lmList =", lmList)
    for index, lm in enumerate(lmList):
        print(index, lm)
    plotPose3D(lmList) 
    