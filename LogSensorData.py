import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import sys
from hx711 import HX711

def cleanAndExit():
    print "Cleaning..."
    GPIO.cleanup()
    print "Bye!"
    sys.exit()

hx = HX711(20, 21)
hx2 = HX711(5, 6)
sensor = Adafruit_DHT.DHT11
gpio = 4

sensors

hx.set_reading_format("LSB", "MSB")
hx2.set_reading_format("LSB", "MSB")

 
hx.reset()
hx.tare()
hx2.reset()
hx2.tare()

while True:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
        val = hx.get_weight(5)
        grams = val/406.773
        oz=grams/35.274
        oz=round(oz,0)
        val2 = hx2.get_weight(5)
        grams2 = val2/406.773
        oz2=grams2/35.274
        oz2=round(oz2,0)
        print 'Urn 1=', oz, 'oz, Urn 2=', oz2, 'oz', ('{0:0.1f}, {1:0.1f}'.format(temperature, humidity))
        hx.power_down()
        hx2.power_down()
        hx.power_up()
        hx2.power_up()
        time.sleep(5.0)
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()