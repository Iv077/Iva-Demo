#Resumen cosas importantes

import opc
import time
import random

leds =[(255,255,255)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#line with one colour or using range(len(led)) para todo pero de fila en fila
for led in range(60):
    leds[led] = (255,0,0)
    time.sleep(.1)
    client.put_pixels(leds)

#for going back 
led = 0
while led<60:
    leds[59-led] = (0,255,0)
    time.sleep(.1)
    client.put_pixels(leds)
    led = led + 1

#para hacer todo de un color pero todas las filas a la vez
led = 0
while led<60:
    for rows in range(6):
        leds[led + rows*60] = (0,0,255)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1

#para hacer todo de un color pero 3 filas desde la izquierda y 3 filas desde la derrecha
led = 0
while led<60:
    for rows in range(3):
        leds[led + rows*60] = (0,255,0)
    for rows in range(3,6):
        leds[59-led + rows*60] = (0,255,0)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1

#para dos colores, uno desde la hizquierda y otro desde la derrecha
#que se paran en el medio
led = 0
while led<30: # si cambio a led<60 al cruzarse se cambian los colores
    for rows in range(6):
        leds[led + rows*60] = (255,255,0)
        leds[59-led + rows*60] = (255,0,0)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1



