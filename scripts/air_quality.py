#!/usr/bin/python3
import board
from busio import I2C
import adafruit_bme680
import mh_z19

from dotenv import dotenv_values
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

# Create library object using our Bus I2C port
i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1033
bme680_temperature_offset = 0

print("### BME860 ###")
print("Temperature: %0.1f C" % (bme680.temperature + bme680_temperature_offset))
print("Gas: %d ohm" % bme680.gas)
print("Humidity: %0.1f %%" % bme680.relative_humidity)
print("Pressure: %0.3f hPa" % bme680.pressure)
print("Altitude = %0.2f meters" % bme680.altitude)
print()

mhz19 = mh_z19.read_all()

print("### MH-Z19B ###")
print(mh_z19.read_all())
print("CO2 = %0.2f " % mhz19['co2'])
print("Temperature = %0.1f C" % mhz19['temperature'])
print("TT = %0.2f " % mhz19['tt'])
print("SS = %0.2f " % mhz19['ss'])
print("UhUl = %0.2f " % mhz19['uhul'])

config = dotenv_values("../.env")
bucket = config['INFLUXDB_BUCKET']
org = config['INFLUXDB_ORG']
token = config['INFLUXDB_TOKEN']
url="http://localhost:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("my_measurement") \
      .tag("location", "Prague") \
      .field("temperature", mhz19['temperature']) \
      .field("humidity", bme680.relative_humidity)  \
      .field("pressure", bme680.pressure)  \
      .field("gas", bme680.gas)  \
      .field("altitude", bme680.altitude)  \
      .field("co2", mhz19['co2'])  \
      .field("tt", mhz19['tt'])  \
      .field("ss", mhz19['ss']) \
      .field("uhul", mhz19['uhul']) 

write_api.write(bucket=bucket, org=org, record=p)

