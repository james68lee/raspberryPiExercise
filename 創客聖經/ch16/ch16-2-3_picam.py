from gpiozero import Motor
from picamera2 import Picamera2
import cv2
import numpy as np
from time import sleep

# Initialize Motors
motor1 = Motor(forward=18, backward=23, pwm=True)
motor2 = Motor(forward=24, backward=25, pwm=True)

def stop():
    motor1.stop()
    motor2.stop()
    
def forward(left_speed=1.0, right_speed=1.0, delay=1):
    motor1.forward(left_speed)
    motor2.forward(right_speed)
    sleep(delay)
    stop()

def backward(left_speed=1.0, right_speed=1.0, delay=1):
    motor1.backward(left_speed)
    motor2.backward(right_speed)
    sleep(delay)
    stop()    
    
def turn_right(speed=0.5, delay=1):
    motor1.forward(speed)
    motor2.stop()
    sleep(delay)
    stop()
        
def turn_left(speed=0.5, delay=1):
    motor1.stop()
    motor2.forward(speed)
    sleep(delay)
    stop()

f_lspeed = 0.45
f_rspeed = 0.5
t_rspeed = 0.5
t_lspeed = 0.59

hue_value = 27
yellow_lower = np.array([hue_value-10, 100, 100], np.uint8)
yellow_upper = np.array([hue_value+10, 255, 255], np.uint8)
kernel = np.ones((7,7), np.uint8)

# Camera setup
camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"size": (640, 480)}))
camera.start()

center_image_x = 640 / 2
center_image_y = 480 / 2

while True:
    frame = camera.capture_array()
    # frame = cv2.flip(frame, -1)  # 是否需翻轉影格
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ball_area = 0
    ball_x = 0
    ball_y = 0
    ball_radius = 0
    for contour in contours:
        x, y, width, height = cv2.boundingRect(contour)
        found_area = width * height
        center_x = x + (width / 2)
        center_y = y + (height / 2)
        if ball_area < found_area:
            ball_area = found_area
            ball_x = int(center_x)
            ball_y = int(center_y)
            ball_radius = int(width / 2)
    if ball_area > 10000:
        print(ball_area)
        cv2.circle(frame, (ball_x, ball_y), ball_radius, (0, 255, 255), 2)
        cv2.circle(frame, (ball_x, ball_y), 5, (0, 0, 255), -1)
        if ball_x > (center_image_x + (640/3)):
            turn_right(t_rspeed, 0.3)
            print("Turning right")
        elif ball_x < (center_image_x - (640/3)):
            turn_left(t_lspeed, 0.3)
            print("Turning left")
        else:
            forward(f_lspeed, f_rspeed, 1)
            print("Forward")
    else:
        stop()
        print("Stop")
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stop()
print("Stop")
cv2.destroyAllWindows()
