from cvzone.PoseModule import PoseDetector
import cv2

detector = PoseDetector()

img = cv2.imread("images/pose.jpg")
img = detector.findPose(img)
lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
if bboxInfo:
    # 計算 11 和 15 的距離
    length, img, info = detector.findDistance(lmList[11][0:2],
                                              lmList[15][0:2],
                                              img=img,
                                              color=(255, 0, 0),
                                              scale=10)
    # 計算 11, 13, 和 15 的角度
    angle, img = detector.findAngle(lmList[11][0:2],
                                    lmList[13][0:2],
                                    lmList[15][0:2],
                                    img=img,
                                    color=(0, 0, 255),
                                    scale=10)
    # 檢查角度是 40~60 度
    isCloseAngle50 = detector.angleCheck(myAngle=angle,
                                         targetAngle=50,
                                         offset=10)
    print(length, isCloseAngle50)

cv2.imshow("CVZone Pose Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()