from gpiozero import MCP3008,LED
from time import sleep

led = LED(18)
photocell = MCP3008(1)

while True:
    print(photocell.value)
    if photocell.value <= 0.50:
        led.on()
    else:
        led.off()
    sleep(0.5)