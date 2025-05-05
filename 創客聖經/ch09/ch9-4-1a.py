from picamera2 import Picamera2

camera2 = Picamera2()
camera2.start_and_capture_file("/home/pi/Pictures/test2.jpg")
