import cv2
import logging
import datetime
import time    
from tflite_runtime.interpreter import Interpreter
import numpy as np
from traffic_objects import *

_SHOW_IMAGE = False

class ObjectsOnRoadProcessor(object):
    """
    This class 1) detects what objects (namely traffic signs and people) are on the road
    and 2) controls the car navigation (speed/steering) accordingly
    """

    def __init__(self,
                 car=None,
                 speed_limit=40,
                 model='model_result/road_signs_quantized.tflite',
                 label='model_result/road_sign_labels.txt',
                 width=640,
                 height=480):
        # model: This MUST be a tflite model that was specifically compiled for Edge TPU.
        # https://coral.withgoogle.com/web-compiler/
        logging.info('Creating a ObjectsOnRoadProcessor...')
        #self.width = width
        #self.height = height

        # initialize car
        self.car = car
        self.speed_limit = speed_limit
        self.speed = speed_limit

        # initialize TensorFlow models
        with open(label, 'r') as f:
            pairs = (l.strip().split(maxsplit=1) for l in f.readlines())
            self.labels = dict((int(k), v) for k, v in pairs)

        self.interpreter = Interpreter(model_path=model)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        self.min_confidence = 0.2
        _, self.height, self.width, _ = self.interpreter.get_input_details()[0]["shape"]

        # initialize open cv for drawing boxes
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.bottomLeftCornerOfText = (10, height - 10)
        self.fontScale = 1
        self.fontColor = (255, 255, 255)  # white
        self.boxColor = (0, 0, 255)  # RED
        self.boxLineWidth = 1
        self.lineType = 2
        self.annotate_text = ""
        self.annotate_text_time = time.time()
        self.time_to_show_prediction = 1.0  # ms

        #
        self.traffic_objects = {0: GreenTrafficLight(),
                                1: Person(),
                                2: RedTrafficLight(),
                                3: SpeedLimit(25),
                                4: SpeedLimit(40),
                                5: StopSign()}

    def process_objects_on_road(self, frame):
        # Main entry point of the Road Object Handler
        logging.debug('Processing objects.................................')
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        objects, final_frame = self.detect_objects(frame)
        self.control_car(objects)
        logging.debug('Processing objects END..............................')

        return final_frame

    def control_car(self, objects):
        logging.debug('Control car...')
        car_state = {"speed": self.speed_limit, "speed_limit": self.speed_limit}

        if len(objects) == 0:
            logging.debug('No objects detected, drive at speed limit of %s.' % self.speed_limit)

        contain_stop_sign = False
        for obj in objects:            
            obj_label = self.labels[obj.label_id]
            print(obj_label)
            processor = self.traffic_objects[obj.label_id]
            if processor.is_close_by(obj, self.height):
                processor.set_car_state(car_state)
            else:
                logging.debug("[%s] object detected, but it is too far, ignoring. " % obj_label)
            if obj_label == 'Stop':
                contain_stop_sign = True

        if not contain_stop_sign:
            self.traffic_objects[5].clear()

        self.resume_driving(car_state)

    def resume_driving(self, car_state):
        old_speed = self.speed
        self.speed_limit = car_state['speed_limit']
        self.speed = car_state['speed']

        if self.speed == 0:
            self.set_speed(0)
        else:
            self.set_speed(self.speed_limit)
        logging.debug('Current Speed = %d, New Speed = %d' % (old_speed, self.speed))

        if self.speed == 0:
            logging.debug('full stop for 1 seconds')
            time.sleep(1)

    def set_speed(self, speed):
        # Use this setter, so we can test this class without a car attached
        self.speed = speed
        if self.car is not None:
            logging.debug("Actually setting car speed to %d" % speed)
            if speed == 0:
                self.car.motor.stop()
            else:
                self.car.motor.move(speed/100.0)

    ############################
    # Frame processing steps
    ############################
    def detect_objects(self, frame):
        logging.debug('Detecting objects...')
        start_ms = time.time()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb, (self.width, self.height))
        input_data = np.expand_dims(frame_resized, axis=0)
        self.interpreter.set_tensor(self.input_details[0]["index"],input_data)
        self.interpreter.invoke()
        boxes = self.interpreter.get_tensor(self.output_details[0]["index"])[0]
        classes = self.interpreter.get_tensor(self.output_details[1]["index"])[0]
        scores = self.interpreter.get_tensor(self.output_details[2]["index"])[0] 
        objects = []
        imHeight = frame.shape[0]
        imWidth = frame.shape[1]
        for i in range(len(scores)):
            if ((scores[i] > self.min_confidence) and (scores[i] <= 1.0)):
                min_y = int(max(1,(boxes[i][0] * imHeight)))
                min_x = int(max(1,(boxes[i][1] * imWidth)))
                max_y = int(min(imHeight,(boxes[i][2] * imHeight)))
                max_x = int(min(imWidth,(boxes[i][3] * imWidth)))              
                cv2.rectangle(frame, (min_x,min_y), (max_x,max_y), (10,255,0), 2)  
                object_name = self.labels[int(classes[i])]
                objects.append(detect_objs(int(classes[i]), boxes))
                label = "%s: %d%%" % (object_name, int(scores[i]*100))
                labelSize, baseLine = cv2.getTextSize(label,
                                      cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
                label_min_y = max(min_x, labelSize[1] + 10)
                cv2.rectangle(frame, (min_x, label_min_y-labelSize[1]-10),
                                 (min_x+labelSize[0], label_min_y+baseLine-10), 
                                 (255, 255, 255), cv2.FILLED) 
                cv2.putText(frame, label, (min_x, label_min_y-7), 
                                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

        if len(objects) == 0:
            logging.debug('No object detected')

        elapsed_ms = time.time() - start_ms

        annotate_summary = "%.1f FPS" % (1.0/elapsed_ms)
        logging.debug(annotate_summary)
        cv2.putText(frame, annotate_summary, self.bottomLeftCornerOfText, self.font, self.fontScale, self.fontColor, self.lineType)
        #cv2.imshow('Detected Objects', frame)

        return objects, frame

class detect_objs:
    # 建構式
    def __init__(self, label_id, bounding_box):
        self.label_id = label_id 
        self.bounding_box = bounding_box
############################
# Utility Functions
############################
def show_image(title, frame, show=_SHOW_IMAGE):
    if show:
        cv2.imshow(title, frame)


############################
# Test Functions
############################
def test_photo(file):
    object_processor = ObjectsOnRoadProcessor()
    frame = cv2.imread(file)
    combo_image = object_processor.process_objects_on_road(frame)
    show_image('Detected Objects', combo_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def test_stop_sign():
    # this simulates a car at stop sign
    object_processor = ObjectsOnRoadProcessor()
    frame = cv2.imread('images/stop_sign.jpg')
    combo_image = object_processor.process_objects_on_road(frame)
    show_image('Stop 1', combo_image)
    time.sleep(1)
    frame = cv2.imread('images/stop_sign.jpg')
    combo_image = object_processor.process_objects_on_road(frame)
    show_image('Stop 2', combo_image)
    time.sleep(2)
    frame = cv2.imread('images/stop_sign.jpg')
    combo_image = object_processor.process_objects_on_road(frame)
    show_image('Stop 3', combo_image)
    time.sleep(1)
    frame = cv2.imread('images/green_light.jpg')
    combo_image = object_processor.process_objects_on_road(frame)
    show_image('Stop 4', combo_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def test_video(video_file):
    object_processor = ObjectsOnRoadProcessor()
    cap = cv2.VideoCapture(video_file + '.avi')

    # skip first second of video.
    for i in range(3):
        _, frame = cap.read()

    video_type = cv2.VideoWriter_fourcc(*'XVID')
    date_str = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    video_overlay = cv2.VideoWriter("%s_overlay_%s.avi" % (video_file, date_str), video_type, 20.0, (320, 240))
    try:
        i = 0
        while cap.isOpened():
            _, frame = cap.read()
            cv2.imwrite("%s_%03d.png" % (video_file, i), frame)

            combo_image = object_processor.process_objects_on_road(frame)
            cv2.imwrite("%s_overlay_%03d.png" % (video_file, i), combo_image)
            video_overlay.write(combo_image)

            cv2.imshow("Detected Objects", combo_image)

            i += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        video_overlay.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)-5s:%(asctime)s: %(message)s')

    # These processors contains no state
    test_photo('images/red_light.jpg')
    test_photo('images/person.jpg')
    test_photo('images/limit_40.jpg')
    test_photo('images/limit_25.jpg')
    #test_photo('images/green_light.jpg')
    test_photo('images/no_obj.jpg')

    # test stop sign, which carries state
    #test_stop_sign()