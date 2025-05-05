from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from time import sleep

camera2 = Picamera2()
camera_config = camera2.create_video_configuration()
camera2.configure(camera_config)
camera2.start_preview(Preview.QTGL)
encoder = H264Encoder()
camera2.start()
video_output = FfmpegOutput("/home/pi/Pictures/test.mp4")
sleep(2)
camera2.start_recording(encoder, output=video_output)
sleep(5)
camera2.stop_recording()
camera2.stop_preview()

