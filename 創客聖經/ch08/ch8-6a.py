import serial

ser = serial.Serial('/dev/ttyACM0', 115200)

while True:
    if ser.in_waiting > 0:
        sensor_value = ser.readline().decode('utf-8').strip()
        print("Sensor Value:", sensor_value)
