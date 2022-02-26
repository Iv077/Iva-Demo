import opc
import time
from time import sleep
import colorsys
import itertools

##num = 10
##for _ in itertools.repeat(None, num):
leds = [(0,0,0)]*360 #black

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

s = 1.0 ##maximum colour
v = 1.0 ##maximum brightness
start_hue = 10 #colour vals

led=0

while True:
    for _ in range(4):
        for i in range(360): #this decides the final value(kind of)
                rgb_fractional = colorsys.hsv_to_rgb(((start_hue+i))/25.0, s, i/60) #colorsys returns floats between 0 and 1
                r,g,b = rgb_fractional #extract said floating point numbers and convert to rgb range
                leds[i] = (r*10,g*139,b*139)
        client.put_pixels(leds) #assign
        sleep(0.3)
        for i in range(360): #this decides the final value(kind of)
                rgb_fractional = colorsys.hsv_to_rgb(((start_hue+i))/25.0, s, i/40) #colorsys returns floats between 0 and 1
                r,g,b = rgb_fractional #extract said floating point numbers and convert to rgb range
                leds[i-60] = (r*10,g*139,b*139)
        client.put_pixels(leds) #assign
        sleep(0.3)
    break
