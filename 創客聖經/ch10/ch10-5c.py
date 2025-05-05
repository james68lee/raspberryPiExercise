from ultralytics import YOLO
import cv2

# 載入NCNN格式的姿態評估與追蹤模型
model = YOLO('yolo11n-pose_ncnn_model')

img = cv2.imread('images/pose.jpg')
results = model(img)
result = results[0].plot()
cv2.imshow('yolo', result)

cv2.waitKey(0)
cv2.destroyAllWindows()