#-*-coding:utf-8-*-

import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()

temp = sensor.read_temperature()
pressure = sensor.read_pressure()
ALTitude = sensor.read_altitude()

print('Temp = {0:0.2f} *C'.format(temp))
print('Pressure = {0:0.2f} Pa'.format(pressure))
print('ALTitude = {0:0.2f} m'.format(ALTitude))
