from gpiozero import MCP3008, PWMLED

led = PWMLED(18)
pot = MCP3008(0)

while True:
    led.value = pot.value