import cv2

cap = cv2.VideoCapture(8)  # 樹莓派5同時連接Pi相機模組是8; 樹莓派4是1, 否則是0

while(cap.isOpened()):
  ret, frame = cap.read()
  cv2.imshow('frame',frame)      
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  
cap.release()
cv2.destroyAllWindows()


