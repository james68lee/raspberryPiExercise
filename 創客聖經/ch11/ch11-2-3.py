from cvzone.FaceMeshModule import FaceMeshDetector
import cv2

detector = FaceMeshDetector(maxFaces=2)

img = cv2.imread("images/face2.jpg")
img, faces = detector.findFaceMesh(img)
if faces:
    print(faces[0])

cv2.imshow("CVZone Face Mesh", img)
cv2.waitKey(0)
cv2.destroyAllWindows()