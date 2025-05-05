import numpy as np
import cv2

hue_value = 180
red_lower = np.array([hue_value-10, 100, 100], np.uint8)
red_upper = np.array([hue_value+10, 255, 255], np.uint8)
kernel = np.ones((7,7), np.uint8)

cap = cv2.VideoCapture(8)  # 樹莓派5同時連接Pi相機模組是8; 樹莓派4是1, 否則是0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, red_lower, red_upper) 
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    balls = cnts[-2]   # 取得輪廓
    # 是否有偵測到
    if len(balls) > 0:
        # 找出最大面積的球
        c = max(balls, key=cv2.contourArea)
        # 取出座標和半徑
        (x, y), radius = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        # 計算出圓心座標
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        # 只處理半徑是 50~300 之間的球
        if (radius < 300) & (radius > 50 ) : 
            # 繪出球的外框
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)  # 繪出中心點
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
