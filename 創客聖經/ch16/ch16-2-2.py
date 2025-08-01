from gpiozero import Motor, DistanceSensor
import cv2
import numpy as np
from time import sleep
import random

# Initialize DistanceSensor
sensor = DistanceSensor(echo=12, trigger=16)

# Initialize Motors
motor1 = Motor(forward=18, backward=23, pwm=True)
motor2 = Motor(forward=24, backward=25, pwm=True)

def stop():
    motor1.stop()
    motor2.stop()

def forward(left_speed=1, right_speed=1, delay=1):
    motor1.forward(left_speed)
    motor2.forward(right_speed)
    sleep(delay)
    stop()

def backward(left_speed=1, right_speed=1, delay=1):
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

cap = cv2.VideoCapture(8)  # 樹莓派5同時連接Pi相機模組是8; 樹莓派4是1, 否則是0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Frame", frame)
    result = sensor.distance * 100  # Convert to cm
    print(result, "cm")
    if result <= 25:  # Obstacle ahead
        if result < 20:  # Too close, back up before turning
            backward(f_lspeed, f_rspeed, 1)
        if random.randint(1, 100) > 50:
            turn_left(t_lspeed, 1)
        else:
            turn_right(t_rspeed, 1)
    else:
        forward(f_lspeed, f_rspeed, 1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stop()
print("Stop")
cap.release()
cv2.destroyAllWindows()
