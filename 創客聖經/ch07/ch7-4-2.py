from gpiozero import PWMLED

led = PWMLED(18)

while True:
    bright = int(input("Enter Brightness(0~100): "))
    led.value = bright / 100.0