#!/usr/bin/env python3
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import sys
from hx711 import HX711
import json
import pprint
import argparse
import sys

pp = pprint.PrettyPrinter(indent=4)

def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()

def initializeHX(dout,pd_sck):
    hxSensor = HX711(dout,pd_sck)
    hxSensor.tare()
    convertUnit = 406.773/0.03527396
    hxSensor.set_reference_unit(convertUnit)
    hxSensor.set_reading_format("LSB", "MSB")
    return hxSensor

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tare", action='store_true', help="Switch to generate and store scale tare")
    args = parser.parse_args()
    hxSensors = [initializeHX(20, 21), initializeHX(5, 6)]

    sensorSettings = {}
    if (args.tare):
        i=0
        for hx in hxSensors:
            hxKey = 'hx{}'.format(i)
            sensorSettings.update({
                hxKey: {
                    'offset': hx.get_offset(),
                    'REFERENCE_UNIT': hx.get_reference_unit()
                }
            })
            i += 1
        with open('settings.json', 'w') as settingsFile:
            json.dump(sensorSettings, settingsFile)
            settings.close()
            sys.exit(0)
    else:
        with open('settings.json', 'r') as settingsFile:
            sensorSettings = json.load(settingsFile)
            settings.close()
        i = 0
        for hx in hxSensors:
            hxKey = 'hx{}'.format(i)
            hx.set_offset(sensorSettings[hxKey]['offset'])
            hx.set_reference_unit(sensorSettings[hxKey]['REFERENCE_UNIT'])
            i += 1

    climSensor = Adafruit_DHT.DHT11
    while True:
        weight = []
        try:
            humidity, temperature = Adafruit_DHT.read_retry(climSensor, 4)
            temperature = temperature*1.8+32
            for hx in hxSensors:
                hx.reset()
                val = hx.get_weight(5)[0]
                weight.append(abs(val))
            sensorResult = {
                'urn1':  round(weight[0],0),
                'urn2': round(weight[1],0),
                'humidity': round(humidity,1),
                'temperature': round(temperature,1),
                'time': datetime.datetime.utcnow()
            }
            #prints json
            with open('/var/log/covfefe/sensorData.json', 'a') as dataFile:
                json.dumps(sensorResult, dataFile)
                dataFile.close()
            #pp.pprint(weight)
            #prints the same line with better formatting
            #print('Urn 1={:1.0f}oz, Urn 2={:1.0f}oz, {:0.1f}, {:0.1f}'.format(weight[0],weight[1],temperature,humidity))
            #print 'Urn 1=', oz, 'oz, Urn 2=', oz2, 'oz', ('{0:0.1f}, {1:0.1f}'.format(temperature, humidity))
            time.sleep(5)
        except (KeyboardInterrupt, SystemExit):
            cleanAndExit()

if __name__ == "__main__":
    main()
