from cvzone.PoseModule import PoseDetector
import cv2

detector = PoseDetector()

img = cv2.imread("images/pose.jpg")
img = detector.findPose(img)
lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
if bboxInfo:
    center = bboxInfo["center"]
    cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

cv2.imshow("CVZone Pose Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()