#GND na GND
#VDD na 3V3
#SCL/SCK na D2
#SDA na D5

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(scl=Pin(2, Pin.OUT), sda=Pin(0, Pin.OUT))
oled = SSD1306_I2C(width=128, height=64, i2c=i2c, addr=0x3c)

oled.line(50, 50, 99, 99, 1)
oled.text("Hello World", 0, 0, 1)
oled.rect(110, 2, 10, 5, 1)
oled.fill_rect(100, 20, 10, 5, 1)

oled.show()
