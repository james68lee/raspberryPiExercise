from picamera2 import Picamera2
from time import sleep

camera2 = Picamera2()
camera_config = camera2.create_still_configuration(
                        main={"size": (640, 480)})
camera2.configure(camera_config)
camera2.start()
sleep(2)
camera2.capture_file("/home/pi/Pictures/size.jpg")
