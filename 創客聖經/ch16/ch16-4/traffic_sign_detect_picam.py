from picamera2 import Picamera2
import cv2
from tflite_runtime.interpreter import Interpreter
import numpy as np

data_folder = "model_result/"

model_path = data_folder + "road_signs_quantized.tflite"
label_path = data_folder + "road_sign_labels.txt"
min_conf_threshold = 0.5
  
with open(label_path, "r") as f:
    labels = [line.strip() for line in f.readlines()]

interpreter = Interpreter(model_path=model_path)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
_, height, width, _ = interpreter.get_input_details()[0]["shape"]
# Camera setup
camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"size": (640, 480)}))
camera.start()
# 取得影像寬度和高度
config = camera.camera_configuration()
imWidth = config["main"]["size"][0]
imHeight = config["main"]["size"][1]

while True:
    frame = camera.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame_rgb, (width, height))
    input_data = np.expand_dims(frame_resized, axis=0)
    interpreter.set_tensor(input_details[0]["index"],input_data)
    interpreter.invoke()
    boxes = interpreter.get_tensor(output_details[0]["index"])[0]
    classes = interpreter.get_tensor(output_details[1]["index"])[0]
    scores = interpreter.get_tensor(output_details[2]["index"])[0] 
    for i in range(len(scores)):
        if ((scores[i] > min_conf_threshold) and (scores[i] <= 1.0)):
            min_y = int(max(1,(boxes[i][0] * imHeight)))
            min_x = int(max(1,(boxes[i][1] * imWidth)))
            max_y = int(min(imHeight,(boxes[i][2] * imHeight)))
            max_x = int(min(imWidth,(boxes[i][3] * imWidth)))              
            cv2.rectangle(frame, (min_x,min_y), (max_x,max_y), (10,255,0), 2)  
            object_name = labels[int(classes[i])] 
            label = "%s: %d%%" % (object_name, int(scores[i]*100))
            labelSize, baseLine = cv2.getTextSize(label,
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
            label_min_y = max(min_x, labelSize[1] + 10)
            cv2.rectangle(frame, (min_x, label_min_y-labelSize[1]-10),
                                 (min_x+labelSize[0], label_min_y+baseLine-10), 
                                 (255, 255, 255), cv2.FILLED) 
            cv2.putText(frame, label, (min_x, label_min_y-7), 
                                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    cv2.imshow("Object Detector", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
