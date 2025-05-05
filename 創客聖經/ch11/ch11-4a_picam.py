from cvzone.HandTrackingModule import HandDetector
from picamera2 import Picamera2
import cv2

detector = HandDetector(detectionCon=0.5, maxHands=1)
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480)}))
picam2.start()

while True:
    img = picam2.capture_array()
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        bbox = hand["bbox"]        
        fingers = detector.fingersUp(hand)
        totalFingers = fingers.count(1)
        print(totalFingers)
        msg = "None"
        if totalFingers == 5:
            msg = "Paper"
        if totalFingers == 0:
            msg = "Rock"
        if totalFingers == 2:
            if fingers[1] == 1 and fingers[2] == 1:
                msg = "Scissors"
        cv2.putText(img, msg, (bbox[0]+200,bbox[1]-30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.imshow("CVZone Hand Detector", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
cv2.destroyAllWindows()
picam2.stop()
