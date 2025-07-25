import cv2

cap = cv2.VideoCapture(8)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20, (640,480))

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):      
      break
  else:
    break

cap.release()
out.release()
cv2.destroyAllWindows()


