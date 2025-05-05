import logging
from pi_car_motor import MotorControl
import cv2
import datetime
from hand_coded_lane_follower import HandCodedLaneFollower
from objects_on_road_processor import ObjectsOnRoadProcessor

_SHOW_IMAGE = True

class DeepPiCar(object):

    __INITIAL_SPEED = 0
    __SCREEN_WIDTH = 640
    __SCREEN_HEIGHT = 480

    def __init__(self):
        """ Init camera and wheels"""
        logging.info('Creating a DeepPiCar...')
        logging.debug('Set up camera')
        self.camera = cv2.VideoCapture(8)    # 樹莓派5同時連接Pi相機模組是8; 樹莓派4是1, 否則是0
        self.camera.set(3, self.__SCREEN_WIDTH)
        self.camera.set(4, self.__SCREEN_HEIGHT)

        self.motor = MotorControl()
        
        self.lane_follower = HandCodedLaneFollower(self)
        #from end_to_end_lane_follower import EndToEndLaneFollower
        #self.lane_follower = EndToEndLaneFollower(self)
        
        self.traffic_sign_processor = ObjectsOnRoadProcessor(self)
       

        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        datestr = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        self.video_orig = self.create_video_recorder('../data/tmp/car_video%s.avi' % datestr)
        self.video_lane = self.create_video_recorder('../data/tmp/car_video_lane%s.avi' % datestr)
        self.video_objs = self.create_video_recorder('../data/tmp/car_video_objs%s.avi' % datestr)

        logging.info('Created a DeepPiCar')

    def create_video_recorder(self, path):
        return cv2.VideoWriter(path, self.fourcc, 20.0, (self.__SCREEN_WIDTH, self.__SCREEN_HEIGHT))

    def __enter__(self):
        """ Entering a with statement """
        return self

    def __exit__(self, _type, value, traceback):
        """ Exit a with statement"""
        if traceback is not None:
            # Exception occurred:
            logging.error('Exiting with statement with exception %s' % traceback)

        self.cleanup()

    def cleanup(self):
        """ Reset the hardware"""
        logging.info('Stopping the car, resetting hardware.')
        self.motor.stop()
        self.camera.release()
        self.video_orig.release()
        self.video_lane.release()
        self.video_objs.release()
        cv2.destroyAllWindows()

    def drive(self, speed=__INITIAL_SPEED):
        """ Main entry point of the car, and put it in drive mode

        Keyword arguments:
        speed -- speed of back wheel, range is 0 (stop) - 100 (fastest)
        """
        logging.info('Starting to drive at speed %s...' % speed)
        self.motor.move(speed/100.0)
        
        fps = int(self.camera.get(5))
        print("Camera fps:", fps)
        
        target = 5   # 1/6    
        counter = 0
        
        while self.camera.isOpened():
            if counter == target: 
                ret, image_lane = self.camera.read()
                counter = 0
            else:
                ret = self.camera.grab() 
                counter += 1
                continue
            if not ret:
                break                    
            image_objs = image_lane.copy()
            self.video_orig.write(image_lane)

        #    image_objs = self.process_objects_on_road(image_objs)
        #    self.video_objs.write(image_objs)
        #    show_image('Detected Objects', image_objs)

            image_lane = self.follow_lane(image_lane)
            self.video_lane.write(image_lane)
            show_image('Lane Lines', image_lane)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.cleanup()
                break

    def process_objects_on_road(self, image):
        image = self.traffic_sign_processor.process_objects_on_road(image)
        return image

    def follow_lane(self, image):
        image = self.lane_follower.follow_lane(image)
        return image


############################
# Utility Functions
############################
def show_image(title, frame, show=_SHOW_IMAGE):
    if show:
        cv2.imshow(title, frame)


def main():
    with DeepPiCar() as car:
        car.drive(30)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)-5s:%(asctime)s: %(message)s')
    
    main()
