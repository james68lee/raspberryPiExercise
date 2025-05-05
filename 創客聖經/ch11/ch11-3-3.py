# from cvzone.PoseModule import PoseDetector
from PoseModule import PoseDetector
import cv2

detector = PoseDetector()

img = cv2.imread("images/pose.jpg")
img = detector.findPose(img)

lmList, bboxInfo = detector.findPosition(img, draw=False, bboxWithHands=False)

if lmList:
    length, img, info = detector.findDistance(lmList[11], lmList[15],
                                              img=img, color=(255, 0, 0),
                                              scale=10)
    length2, img, info = detector.findDistance3D(lmList[12], lmList[16],
                                              img=img, color=(255, 255, 0),
                                              scale=5)
    print(length, length2)

cv2.imshow("CVZone Pose Detector", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
   
    