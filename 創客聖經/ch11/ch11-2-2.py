from cvzone.FaceDetectionModule import FaceDetector
import cv2

detector = FaceDetector()

img = cv2.imread("images/face.jpg")
img, bboxs = detector.findFaces(img)
if bboxs:
    # bboxInfo - "id","bbox","score","center"
    center = bboxs[0]["center"]
    cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

cv2.imshow("CVZone Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()