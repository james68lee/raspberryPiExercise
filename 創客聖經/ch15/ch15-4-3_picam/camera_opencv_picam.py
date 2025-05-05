import os
import cv2
from base_camera import BaseCamera
from picamera2 import Picamera2

class Camera(BaseCamera):

    def __init__(self):
        super(Camera, self).__init__()

    @staticmethod
    def frames():
        camera = Picamera2()
        camera.configure(
            camera.create_still_configuration(main={"size": (320, 240)}))
        try:
            camera.start()
        except Exception as e:
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            img = camera.capture_array()
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
