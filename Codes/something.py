
import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
led=0

led = 0
while led<60:                 #hacer el movimiento para siempre 
    for led in range(52):   # en que rango quiero que el movimiento ocurra
        if 'A':
            leds = [(0,0,0)]*360      #todo de un color
            leds[351-led] = (255,0,0)
            leds[351-led+8] = (255,0,0) 
            leds[292-led] = (255,0,0)
            leds[292-led+6] = (255,0,0)
            leds[233-led] = (255,0,0)
            leds[233-led+2] = (255,0,0)
            leds[233-led+4] = (255,0,0)
            leds[174-led] = (255,0,0)
            leds[174-led+2] = (255,0,0)
            leds[115-led] = (255,0,0)
            client.put_pixels(leds)
            time.sleep(.1)
            break
        if 'B':
            leds = [(0,0,0)]*360    
            leds[351-led] = (255,0,0)
            leds[351-led+2] = (255,0,0)
            leds[351-led+4] = (255,0,0)
            leds[291-led] = (255,0,0)
            leds[291-led+6] = (255,0,0)
            leds[231-led] = (255,0,0)
            leds[231-led+4] = (255,0,0)
            leds[231-led+3] = (255,0,0)
            leds[231-led+2] = (255,0,0)
            leds[171-led] = (255,0,0)
            leds[171-led+6] = (255,0,0)
            leds[111-led] = (255,0,0)
            leds[111-led+2] = (255,0,0)
            leds[111-led+4] = (255,0,0)
            client.put_pixels(leds)
            time.sleep(.1)
            break
        
