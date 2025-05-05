from umqtt.simple import MQTTClient
from machine import Pin
import dht
import network
import utime

def connect_wifi(ssid, passwd):
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    if not sta.isconnected():
       print("Connecting to network...")
       sta.connect(ssid, passwd)
       while not sta.isconnected():
          pass
    print("network config:", sta.ifconfig())
    
SSID = "<WiFi名稱>"        # WiFi名稱
PASSWORD = "<WiFi密碼>"    # WiFi密碼
connect_wifi(SSID, PASSWORD)
sensor = dht.DHT11(Pin(22))

# MQTT 客戶端
client = MQTTClient (
    client_id = "mqtt1234_dht11",
    server = "broker.hivemq.com",
    ssl = False,
)
client.connect()  # 連線MQTT
topic_temp = "sensors/1234/temp"
topic_humi = "sensors/1234/humi"

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        client.publish(topic_temp, str(temp))
        humid = sensor.humidity()
        client.publish(topic_humi, str(humid))
        utime.sleep(2)
    except OSError as e:
        print("Error reading from DHT11 sensor!")   
