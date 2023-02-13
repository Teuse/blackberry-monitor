import RPi.GPIO as GPIO
import mh_z19
 
PIN_RED = 37
PIN_GREEN = 40
PIN_BLUE = 38
PINS = [PIN_RED, PIN_GREEN, PIN_BLUE]  # R,G,B
 
mhz19 = mh_z19.read_all()
co2 = mhz19['co2']


GPIO.setmode(GPIO.BOARD)
GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)

if co2 > 800 and co2 < 1000:
    GPIO.output(PIN_GREEN, 1)
elif co2 > 1000 and co2 < 1400:
    GPIO.output(PIN_BLUE, 1)
elif co2 > 1400:
    GPIO.output(PIN_RED, 1)
