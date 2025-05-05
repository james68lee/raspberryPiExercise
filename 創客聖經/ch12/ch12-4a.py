from tflite_runtime.interpreter import Interpreter 
import cv2
import numpy as np
import time

# data_folder = "/home/pi/ch12/ssd_mobilenet/"
data_folder = "ssd_mobilenet/"
model_path = data_folder + "lite-model_ssd_mobilenet_v1_1_metadata_2.tflite"
label_path = data_folder + "labelmap.txt"
min_conf_threshold = 0.5

with open(label_path, "r") as f:
    labels = [line.strip() for line in f.readlines()]
interpreter = Interpreter(model_path=model_path)
print("成功載入模型...")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
_, height, width, _ = interpreter.get_input_details()[0]["shape"]
print("圖片資訊: (", width, ",", height, ")")

time1 = time.time()
image = cv2.imread("images/horse.jpg")
#image = cv2.imread("images/koala.jpg")
#image = cv2.imread("images/test.jpg")
imgHeight, imgWidth, _ = image.shape
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_resized = cv2.resize(image_rgb, (width, height))
input_data = np.expand_dims(image_resized, axis=0)
interpreter.set_tensor(input_details[0]["index"],input_data)
interpreter.invoke()
boxes = interpreter.get_tensor(output_details[0]["index"])[0]
classes = interpreter.get_tensor(output_details[1]["index"])[0]
scores = interpreter.get_tensor(output_details[2]["index"])[0] 

time2 = time.time()
classification_time = np.round(time2-time1, 3)
print("辨識時間 =", classification_time, "秒")

for i in range(len(scores)):
    if ((scores[i] > 0.5) and (scores[i] <= 1.0)):
         min_y = int(max(1,(boxes[i][0] * imgHeight)))
         min_x = int(max(1,(boxes[i][1] * imgWidth)))
         max_y = int(min(imgHeight,(boxes[i][2] * imgHeight)))
         max_x = int(min(imgWidth,(boxes[i][3] * imgWidth)))              
         cv2.rectangle(image, (min_x,min_y), (max_x,max_y), (10,255,0), 2)  
         object_name = labels[int(classes[i])]
         label = "%s: %d%%" % (object_name, int(scores[i]*100))
         labelSize, baseLine = cv2.getTextSize(label,
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
         label_min_y = max(min_x, labelSize[1] + 10)
         cv2.rectangle(image, (min_x, label_min_y-labelSize[1]-10),
                              (min_x+labelSize[0], label_min_y+baseLine-10), 
                              (255, 255, 255), cv2.FILLED) 
         cv2.putText(image, label, (min_x, label_min_y-7), 
                              cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
         
cv2.imshow("Object Detector", image)
cv2.waitKey(0)
cv2.destroyAllWindows()         
         
         
         