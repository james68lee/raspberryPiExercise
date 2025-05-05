# from cvzone.HandTrackingModule import HandDetector
from HandTrackingModule import HandDetector
import cv2

detector = HandDetector(detectionCon=0.5, maxHands=2)

img = cv2.imread("images/hands.jpg")
hands, img = detector.findHands(img)
if hands:
    # Hand 1
    hand1 = hands[0]
    lmList1 = hand1["lmList"]
    if len(hands) == 2:
        # Hand 2
        hand2 = hands[1]
        lmList2 = hand2["lmList"]
        length1, img, info = detector.findDistance(
                          lmList1[4], lmList2[20], img)
        length2, img, info = detector.findDistance3D(
                          lmList1[4], lmList2[20], img)
        print(length1, length2)

cv2.imshow("CVZone Hand Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()