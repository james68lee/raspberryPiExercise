from machine import Pin, ADC
import time

sensor = ADC(Pin(27))

while True:
    sensor_value = sensor.read_u16()
    print(sensor_value)
    time.sleep(1)
