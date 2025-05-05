import cv2
import numpy as np

#image = cv2.imread("images/road_lane.jpg")
image = cv2.imread("images/bluetape.jpg")
copy = np.copy(image)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hsv = cv2.GaussianBlur(hsv, (5, 5), 0)
hue_value = 25
yellow_lower = np.array([hue_value-10, 100, 100], np.uint8)
yellow_upper = np.array([hue_value+10, 255, 255], np.uint8)
mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
blue_lower = np.array([30, 40, 0], np.uint8)
blue_upper = np.array([150, 255, 255], np.uint8)
mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)
mask_yb = cv2.bitwise_or(mask_blue, mask_yellow)
cv2.imshow("Mask Yellow/Blue", mask_yb)
edges = cv2.Canny(mask_yb, 50, 150)
cv2.imshow("Road Lane edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()