#!/usr/bin/python3

import random

temperature = round(random.uniform(10.0, 30.0), 2)
pressure = round(random.uniform(800.0, 1100.0), 2)
humidity = round(random.uniform(0.0, 1.0), 2)
quality = round(random.uniform(100000.0, 200000.0), 2)

print("air_quality,dummy=true temperature=" + str(temperature) + ",pressure=" + str(pressure) + ",humidity=" + str(humidity) + ",quality=" + str(quality))