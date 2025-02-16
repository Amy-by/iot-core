# -*- coding: utf-8 -*-
import random
import time

while True:
    # 温度模拟（20±5℃，保留1位小数）
    temp = round(20 + random.uniform(-5, 5), 1)
    # 湿度模拟（50±10%，保留1位小数）
    humidity = round(50 + random.uniform(-10, 10), 1)
    # 生成伪造数据
    fake_data = f"{time.ctime()}, Temperature: {temp}°C, Humidity: {humidity}%"
    print(fake_data)
    time.sleep(5)
