import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import sys
from hx711 import HX711

class hx:
    scale = 0
    def __init_(r,c):
        scale = r*c


class scales:

class sensors:
    hum = 70
    temp = 80
    scale1 = 10000
    scale2 = 20000
    #Get Grams
    def get_grams():
    #Get Oz
    #Get Temp
    #Get Humdity

    #initalize Sensors
    def __init__(self):





def cleanAndExit():
    print "Cleaning..."
    GPIO.cleanup()
    print "Bye!"
    sys.exit()

sensors = {
    climSensor = {
        sensor = Adafruit_DHT.DHT11,
        humidity = 0;
        temperature = 0;
    },
    scales = [
        {
            hx = HX711(20, 21),
            oz = 0
        },
        {
            hx = HX711(5, 6),
            oz = 0
        }
    ]
}

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