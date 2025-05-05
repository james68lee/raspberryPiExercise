from cvzone.HandTrackingModule import HandDetector
import cv2

detector = HandDetector(detectionCon=0.5, maxHands=1)
img = cv2.imread("images/Scissors.png", cv2.IMREAD_COLOR)

hands, img = detector.findHands(img)
if hands:
    hand = hands[0]
    fingers = detector.fingersUp(hand)
    print(fingers)
    totalFingers = fingers.count(1)
    if totalFingers == 5:
        print("Paper")
    if totalFingers == 0:
        print("Rock")
    if totalFingers == 2:
        if fingers[1] == 1 and fingers[2] == 1:
            print("Scissors")
            
cv2.imshow("CVZone Hand Detector", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
