import paho.mqtt.client as mqtt
import random
import time

# MQTT 客戶端
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,
                     client_id="mqtt_test_1234")
broker = "broker.hivemq.com"
topic = "sensors/1234/temp"

def on_message(client, userdata, message):
    print("收到訊息: ", message.payload.decode())

client.on_message = on_message  # 指定回撥函數來接收訊息
client.connect(broker)          # 連線 MQTT 代理人
client.subscribe(topic)         # 訂閱主題

client.loop_start()  # 開始事件迴圈

while True:
    client.publish(topic, str(random.randint(20, 50)))
    time.sleep(2)
    client.loop_read()  # 處理接收訊息

  
