#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
from gpiozero import Motor
from time import sleep

# import camera driver
#if os.environ.get('CAMERA'):
#    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
#else:
#    from camera import Camera

# Raspberry Pi camera module (requires picamera package)
#from camera_pi import Camera
# OpenCV Webcam
from camera_opencv import Camera
# OpenCV Pi camera module
#from camera_opencv_picam import Camera

app = Flask(__name__)

motor1 = Motor(forward=18, backward=23, pwm=True)
motor2 = Motor(forward=24, backward=25, pwm=True)

delay = 1

def stop():
    motor1.stop()
    motor2.stop()
    
def forward(speed=1.0):
    motor1.forward(speed)
    motor2.forward(speed)

def backward(speed=1.0):
    motor1.backward(speed)
    motor2.backward(speed)   
    
def turn_right(speed=0.5):
    motor1.forward(speed)   
    motor2.stop()   
    
def turn_left(speed=0.5): 
    motor1.stop()
    motor2.forward(speed)  
    
speed = 0.5

@app.route("/f")
def go_forward():
    forward(speed)
    sleep(delay)
    stop()
    return "Forward..."

@app.route("/b")
def go_backward():
    backward(speed)
    sleep(delay)
    stop()
    return "Backward..."

@app.route("/r")
def go_turn_right():
    turn_right(speed)
    sleep(delay)
    stop()
    return "Turn Right..."
    
@app.route("/l")
def go_turn_left():
    turn_left(speed)
    sleep(delay)
    stop()
    return "Turn Left..."

@app.route("/s")
def go_stope():
    stop()
    return "Stop..."
    
@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
