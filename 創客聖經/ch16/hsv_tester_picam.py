from picamera2 import Picamera2
import time
import cv2
import numpy as np

# Camera setup
camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"size": (640, 480)}))
camera.start()

to_do = True

while to_do:
    hue_value = int(input("Input Hue value (10~245): "))
    if (hue_value < 10) or (hue_value > 245):
        hue_value = 10
    print("Hue value=", hue_value)
    lower = np.array([hue_value-10, 100, 100])
    upper = np.array([hue_value+10, 255, 255])
    kernel = np.ones((7,7), np.uint8)
    
    while True:
        frame = camera.capture_array()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("Color Mask", mask)
        cv2.imshow("Final Result", result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            to_do = False
            break

cv2.destroyAllWindows()

