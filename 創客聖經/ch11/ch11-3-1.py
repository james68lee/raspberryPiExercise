from cvzone.HandTrackingModule import HandDetector
import cv2

detector = HandDetector(detectionCon=0.5, maxHands=2)

img = cv2.imread("images/hands.jpg")
hands, img = detector.findHands(img)
if hands:
    # Hand 1
    hand1 = hands[0]
    lmList = hand1["lmList"]
    print("lmList =", lmList)
    for index, lm in enumerate(lmList):
        print(index, lm)
