from gpiozero import Motor
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

#forward(f_lspeed, f_rspeed, 1)
stop()
t_rspeed = 0.5
t_lspeed = 0.59
# 90度
turn_right(t_rspeed, 1)
stop()
turn_left(t_lspeed, 1)
