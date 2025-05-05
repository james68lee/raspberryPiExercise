# from cvzone.PoseModule import PoseDetector
from PoseModule import PoseDetector
import cv2

detector = PoseDetector()

img = cv2.imread("images/pose.jpg")
img = detector.findPose(img)

lmList, bboxInfo = detector.findPosition(img, draw=False, bboxWithHands=False)

if lmList:
    print(lmList)
    angle, img = detector.findAngle(lmList[24], lmList[26], lmList[28],
                                    img=img, color=(0, 0, 255),
                                    scale=10)
    angle2, img = detector.findAngle3D(lmList[24], lmList[26], lmList[28],
                                       img=img, color=(0, 255, 255),
                                       scale=5)
    print(angle, angle2)
    # 檢查角度是否接近指定角度80度上下10度, 即位在70~90度之間
    isCloseAngle80 = detector.angleCheck(myAngle=angle,
                                         targetAngle=80,
                                         offset=10)
    print(isCloseAngle80)

cv2.imshow("CVZone Pose Detector", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
   
    