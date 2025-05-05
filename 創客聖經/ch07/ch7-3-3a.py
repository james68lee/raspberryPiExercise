from gpiozero import LED, Button
from time import sleep

led = LED(18)
btn = Button(2)

while True:
    btn.wait_for_press()
    led.toggle()
    sleep(0.5)