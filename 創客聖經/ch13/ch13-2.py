from machine import Pin
import utime
import dht 

sensor = dht.DHT11(Pin(22))

while True:
    try:
        utime.sleep(2)
        sensor.measure()
        print("Temperature: ", sensor.temperature(),"\u2103")
        print("Humidity: ", sensor.humidity(), "%")
        print("------------")
    except OSError as e:
        print("Error reading from DHT11 sensor!")
