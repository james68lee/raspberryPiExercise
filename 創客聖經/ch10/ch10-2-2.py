import cv2

cap = cv2.VideoCapture('YouTube.mp4')

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret:
      cv2.imshow('frame',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()


