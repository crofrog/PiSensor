import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import sys
from hx711 import HX711
import json

def cleanAndExit():
    print "Cleaning..."
    GPIO.cleanup()
    print "Bye!"
    sys.exit()

def initializeHX(dout,pd_sck):
    hxSensor = HX711(dout,pd_sck)
    hxSensor.set_reference_unit = 406.773*35.274
    hxSensor.set_reading_format("LSB", "MSB")
    hxSensor.tare()
    return hxSensor

def main():
    hxSensors = [initializeHX(20,21), initializeHX(5,6)]
    climSensor = Adafruit_DHT.DHT11

    while True:
        weight = []
        try:
            humidity, temperature = climSensor.read_retry(sensor, 4)
            for hx in hxSensors:
                hx.reset()
                weight.append(hx.get_weight())
            sensorResult = {
                'urn1':  round(weight[0],0),
                'urn2': round(weight[1],0),
                'humidity': round(humidity,1),
                'temperature': round(temperature,1)
            }
            #prints json
            json.dumps(sensorResult)

            #prints the same line with better formatting
            print('Urn 1={:1.0f}pz, Urn 2={:1.0f}oz, {:0.1f}, {0.1f}'.format(weight[0],weight[1],temperature,humidity)
            #print 'Urn 1=', oz, 'oz, Urn 2=', oz2, 'oz', ('{0:0.1f}, {1:0.1f}'.format(temperature, humidity))
            time.sleep(5.0)
        except (KeyboardInterrupt, SystemExit):
            cleanAndExit()

if __name__ == "__main__":
    main()
