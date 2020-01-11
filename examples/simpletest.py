#!/usr/bin/python
import Adafruit_DHT
import time
# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT22
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


while True:
    if humidity is not None and temperature is not None:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        time.sleep(4)
    else:
        print('Failed to get reading. Try again!')
        
