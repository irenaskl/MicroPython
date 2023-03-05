from time import sleep
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20

pin = Pin(2, Pin.IN)
ow = DS18X20(OneWire(pin))
sensory = ow.scan()
print('Pipojene teplomery:', sensory)

ow.convert_temp()
sleep(1)
teplota = ow.read_temp(sensory[0])
print('Teplota je', teplota)
