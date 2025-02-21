import time
import random
from tb_device_mqtt import TBDeviceMqttClient

# 设备访问令牌
ACCESS_TOKEN = "8JNyEuuwHbnv0gBRtZGR"

# 连接ThingsBoard Cloud
client = TBDeviceMqttClient("thingsboard.cloud", 1883, ACCESS_TOKEN)
client.connect()

# 伪造数据
while True:
    temperature = 25 + random.uniform(-5, 5)
    humidity = 50 + random.uniform(-10, 10)
    client.send_telemetry({"temperature": temperature, "humidity": humidity})
    print(f"上传数据：温度={temperature:.1f}℃, 湿度={humidity:.1f}%")
    time.sleep(5)
