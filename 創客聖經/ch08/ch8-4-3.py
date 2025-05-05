from machine import Pin, PWM
import time

pwm = PWM(Pin(15))
pwm.freq(1000)
while True:
    duty = int(input("Enter Brightness(0~100):"))
    bright = int(duty*655.36)
    print("Brightness: ", bright)
    pwm.duty_u16(bright)
    time.sleep(1)