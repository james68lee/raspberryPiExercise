from cvzone.HandTrackingModule import HandDetector
import cv2

detector = HandDetector(detectionCon=0.5, maxHands=1)

img = cv2.imread("images/hand.jpg")
hands, img = detector.findHands(img)
if hands:
    hand = hands[0]
    bbox = hand['bbox']        
    fingers = detector.fingersUp(hand)
    totalFingers = fingers.count(1)
    cv2.putText(img, f'Fingers:{totalFingers}',
                (bbox[0]+100,bbox[1]-30),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

cv2.imshow("CVZone Hand Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()