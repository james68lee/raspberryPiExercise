# from cvzone.HandTrackingModule import HandDetector
from HandTrackingModule import HandDetector
import cv2

detector = HandDetector(detectionCon=0.5, maxHands=2)

img = cv2.imread("images/hand3.jpg")
hands, img = detector.findHands(img)
if hands:
    # Hand 1
    hand1 = hands[0]
    lmList = hand1["lmList"]
    angle, img = detector.findAngle(lmList[5], lmList[6], lmList[7],
                                    img=img, color=(0,0,255), scale=10)
    angle2, img = detector.findAngle3D(lmList[5], lmList[6], lmList[7],
                                       img=img, color=(0,255,255), scale=5)
    print(angle, angle2)
    # 檢查角度是否接近指定角度100度上下10度, 即位在90~110度之間
    isCloseAngle100 = detector.angleCheck(myAngle=angle,
                                          targetAngle=100,
                                          offset=10)
    print(isCloseAngle100)

cv2.imshow("CVZone Hand Detector", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
   
    