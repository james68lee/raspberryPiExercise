from gpiozero import Motor
from time import sleep

class MotorControl():
    def __init__(self, in1=18, in2=23, in3=24, in4=25):
        self.motor1 = Motor(forward=in1, backward=in2, pwm=True)
        self.motor2 = Motor(forward=in3, backward=in4, pwm=True)
        
        self.left_speed = 0.26
        self.right_speed = 0.29
        self.MINI_SPEED = 0.25
        self.current_speed = 0.40
        
    def stop(self, delay=0):
        self.motor1.stop()
        self.motor2.stop()
        sleep(delay)
    
    def forward(self, left_speed=1.0, right_speed=1.0):
        self.motor1.forward(left_speed)
        self.motor2.forward(right_speed)

    def backward(self, left_speed=1.0, right_speed=1.0):
        self.motor1.backward(left_speed)
        self.motor2.backward(right_speed)
        
    def move(self, speed=0.40, left_inc=0, right_inc=0, dir=True, delay=0):
        self.current_speed = speed
        lspeed = self.left_speed + (speed - self.MINI_SPEED) + left_inc
        rspeed = self.right_speed + (speed - self.MINI_SPEED) + right_inc        
        if lspeed < 0: lspeed = 0
        if lspeed > 1: lspeed = 1
        if rspeed < 0: rspeed = 0
        if rspeed > 1: rspeed = 1
        print(lspeed, rspeed)
        if dir:   # forward
            self.forward(lspeed, rspeed)
        else:     # backward
            self.backward(lspeed, rspeed)
        sleep(delay)

    def turn_angle(self, angle=90):
        weights = 5
        if angle > 90:
            # turn right
            inc = (angle - 90)
            inc = inc // 2 + weights
            self.move(self.current_speed, left_inc=inc/100.0, right_inc=-(inc/100.0))  
        if angle < 90:
            # turn left
            inc = (90 - angle)
            inc = inc // 2 + weights
            self.move(self.current_speed, right_inc=inc/100.0, left_inc=-(inc/100.0))
        sleep(0.2)
        self.move(self.current_speed)
 
if __name__ == '__main__':
    m = MotorControl()
    #m.move(0.40)
    #sleep(2)
    #m.turn_angle(135)
    m.turn_angle(45)
    m.stop()
