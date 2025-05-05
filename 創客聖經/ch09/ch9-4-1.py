from picamera2 import Picamera2, Preview
from time import sleep

camera2 = Picamera2()
camera_config = camera2.create_preview_configuration()
camera2.configure(camera_config)
camera2.start_preview(Preview.QTGL)
camera2.start()
sleep(2)
camera2.capture_file("/home/pi/Pictures/test.jpg")
camera2.stop_preview()
