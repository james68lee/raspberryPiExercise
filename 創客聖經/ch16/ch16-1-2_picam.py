from picamera2 import Picamera2
import cv2
import numpy as np

hue_value = 27
yellow_lower = np.array([hue_value-10, 100, 100], np.uint8)
yellow_upper = np.array([hue_value+10, 255, 255], np.uint8)
kernel = np.ones((7,7), np.uint8)

# Camera setup
camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"size": (640, 480)}))
camera.start()

while True:
    frame = camera.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    balls = cnts[-2]  # 取得輪廓
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
        if 50 < radius < 300:
            # 繪出球的外框
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)  # 繪出中心點
    
    cv2.imshow("Image", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

