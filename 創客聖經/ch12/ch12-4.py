from tflite_runtime.interpreter import Interpreter 
import cv2
import numpy as np

# data_folder = "/home/pi/ch12/ssd_mobilenet/"
data_folder = "ssd_mobilenet/"

model_path = data_folder + "lite-model_ssd_mobilenet_v1_1_metadata_2.tflite"
label_path = data_folder + "labelmap.txt"
min_conf_threshold = 0.5
  
with open(label_path, "r") as f:
    labels = [line.strip() for line in f.readlines()]

interpreter = Interpreter(model_path=model_path)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
_, height, width, _ = interpreter.get_input_details()[0]["shape"]

cap = cv2.VideoCapture(8)  # 樹莓派5同時連接Pi相機模組是8; 樹莓派4是1, 否則是0
imWidth  = cap.get(cv2.CAP_PROP_FRAME_WIDTH) 
imHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 
while cap.isOpened():
    success, frame = cap.read()
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

cap.release()
cv2.destroyAllWindows()
