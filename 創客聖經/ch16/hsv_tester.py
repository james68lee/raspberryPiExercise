import cv2
import numpy as np

hue_value = int(input("Input Hue value (10~245): "))
if (hue_value < 10) or (hue_value > 245):
    hue_value = 10
print("Hue value=", hue_value)
lower = np.array([hue_value-10,100,100])
upper = np.array([hue_value+10, 255, 255])    
kernel = np.ones((7,7), np.uint8)

cap = cv2.VideoCapture(8)  # 樹莓派5同時連接Pi相機模組是8; 樹莓派4是1, 否則是0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)   
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Color Mask", mask)
    cv2.imshow("Final Result", result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()