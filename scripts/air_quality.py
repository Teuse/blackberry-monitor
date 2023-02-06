#!/usr/bin/python3
import board
from busio import I2C
import adafruit_bme680
from . import mh_z19

# Create library object using our Bus I2C port
i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1033

# You will usually have to add an offset to account for the temperature of
# the sensor. This is usually around 5 degrees but varies by use. Use a
# separate temperature sensor to calibrate this one.
#temperature_offset = -5
temperature_offset = 0

temperature = bme680.temperature + temperature_offset

mhz19 = mh_z19.get_all()

print("### BME860 ###")
print("Temperature: %0.1f C" % temperature)
print("Gas: %d ohm" % bme680.gas)
print("Humidity: %0.1f %%" % bme680.relative_humidity)
print("Pressure: %0.3f hPa" % bme680.pressure)
print("Altitude = %0.2f meters" % bme680.altitude)
print()

print("### MH-Z19B ###")
print(mh_z19.read_all())
print("CO2 = %0.2f " % mhz19.co2)
print("Temperature = %0.1f C" % mhz19.temperature)
print("TT = %0.2f " % mhz19.tt)
print("SS = %0.2f " % mhz19.ss)
print("UhUl = %0.2f " % mhz19.uhul)
