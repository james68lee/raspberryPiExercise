import cv2
import numpy as np

img = cv2.imread("images/balls.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 黃色的範圍
yellow_lower = np.array([17, 100, 100], np.uint8)
yellow_upper = np.array([37, 255, 255], np.uint8)
# 建立遮罩
mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
# 刪除遮罩的雜訊
kernel = np.ones((7, 7), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
# 分割出偵測到的區域
segmented_img = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Segmented Image", segmented_img)
# 使用遮罩來找出輪廓
contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 在偵測到的區域繪出輪廓
output_segmented = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
cv2.imshow("Segmented Output", output_segmented)
# 在原始圖片繪出輪廓
output_original = cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
cv2.imshow("Original Output", output_original)
cv2.waitKey(0)
cv2.destroyAllWindows()