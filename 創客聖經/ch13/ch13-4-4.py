from umqtt.simple import MQTTClient
import network
import urandom, math
import utime

def random_in_range(low=0, high=1000):
    r1 = urandom.getrandbits(32)
    r2 = r1 % (high-low) + low
    return math.floor(r2)

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


# MQTT 客戶端
client = MQTTClient (
    client_id = "mqtt_test_1234",
    server = "broker.hivemq.com",
    ssl = False
)
topic = "sensors/1234/temp"

def sub_cb(topic, msg):
    print("收到訊息: ", msg.decode())

client.set_callback(sub_cb)   # 指定回撥函數來接收訊息
client.connect()              # 連線 MQTT 代理人
client.subscribe(topic)       # 訂閱主題

while True:
    client.publish(topic, str(random_in_range(20, 50)))
    utime.sleep(2)
    client.check_msg()
  
