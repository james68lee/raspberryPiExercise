from picamera2 import Picamera2
from libcamera import Transform
from time import sleep

camera2 = Picamera2()
camera_config = camera2.create_still_configuration(
                        main={"size": (640, 480)},
                        transform=Transform(vflip=True, 
                                            hflip=True))
camera2.configure(camera_config)
camera2.set_controls({"Brightness": 0.2})  # -1.0~1.0
camera2.start()
sleep(2)
camera2.capture_file("/home/pi/Pictures/brightness.jpg")
