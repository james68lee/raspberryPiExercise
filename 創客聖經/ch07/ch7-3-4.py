from gpiozero import MotionSensor, LED
from time import sleep

led = LED(18)
pir = MotionSensor(22)

while True:
    if pir.motion_detected:
        led.on()
        print("You moved!")
    else:
        led.off()
    sleep(0.5)   
