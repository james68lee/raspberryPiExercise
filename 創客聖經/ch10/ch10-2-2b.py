import cv2

cap = cv2.VideoCapture('YouTube.mp4')

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret:
      gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',gray_frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()


