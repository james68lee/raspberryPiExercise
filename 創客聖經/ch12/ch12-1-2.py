from tflite_runtime.interpreter import Interpreter 
import cv2
import numpy as np
import time

# data_folder = "/home/pi/ch12/mobilenet/"
data_folder = "mobilenet/"
model_path = data_folder + "mobilenet_v1_1.0_224_quantized_1_metadata_1.tflite"
label_path = data_folder + "labels.txt"

interpreter = Interpreter(model_path)
print("成功載入模型...")
interpreter.allocate_tensors()
_, height, width, _ = interpreter.get_input_details()[0]["shape"]
print("圖片資訊: (", width, ",", height, ")")

time1 = time.time()

image = cv2.imread("images/test.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_resized = cv2.resize(image_rgb, (width, height))
input_data = np.expand_dims(image_resized, axis=0)
interpreter.set_tensor(interpreter.get_input_details()[0]["index"],input_data)
interpreter.invoke()
output_details = interpreter.get_output_details()[0]
output = np.squeeze(interpreter.get_tensor(output_details["index"]))
scale, zero_point = output_details["quantization"]
output = scale * (output - zero_point)
ordered = np.argpartition(-output, 1)
label_id, prob = [(i, output[i]) for i in ordered[:1]][0]

time2 = time.time()
classification_time = np.round(time2-time1, 3)
print("辨識時間 =", classification_time, "秒")

with open(label_path, "r") as f:
    labels = [line.strip() for i, line in enumerate(f.readlines())]
classification_label = labels[label_id]
print("圖片標籤 =", classification_label)
print("辨識準確度 =", np.round(prob*100, 2), "%")