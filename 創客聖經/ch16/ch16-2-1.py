from gpiozero import DistanceSensor
from time import sleep

TRIGGER_PIN = 16
ECHO_PIN = 12
MAX_DISTANCE = 5

sensor = DistanceSensor(echo=ECHO_PIN,
                        trigger=TRIGGER_PIN,
                        max_distance=MAX_DISTANCE)

while True:
    distance = int(sensor.distance * 100) 
    print(distance, "cm")
    sleep(1)
