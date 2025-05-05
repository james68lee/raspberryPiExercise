import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection(
                      min_detection_confidence=0.5)

img = cv2.imread("images/face.jpg")
results = face_detection.process(img)
if results.detections:
    for detection in results.detections:
        mp_drawing.draw_detection(img, detection)

cv2.imshow("MediaPipe Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
