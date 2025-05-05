import cv2
import numpy as np

image = cv2.imread("images/bluetape.jpg")
copy = np.copy(image)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hsv = cv2.GaussianBlur(hsv, (5, 5), 0)
blue_lower = np.array([30, 40, 0], np.uint8)
blue_upper = np.array([150, 255, 255], np.uint8)
mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)
cv2.imshow("Mask Blue", mask_blue)
edges = cv2.Canny(mask_blue, 50, 150)
cv2.imshow("Road Lane edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()