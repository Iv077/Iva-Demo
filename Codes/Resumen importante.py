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
    time.sleep(.01)
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
    time.sleep(.01)
    led = led + 1

#para hacer todo de un color pero 3 filas desde la izquierda y 3 filas desde la derrecha
led = 0
while led<60:
    for rows in range(3):
        leds[led + rows*60] = (0,255,0)
    for rows in range(3,6):
        leds[59-led + rows*60] = (0,255,0)
    client.put_pixels(leds)
    time.sleep(.01)
    led = led + 1

#para dos colores, uno desde la hizquierda y otro desde la derrecha
#que se paran en el medio
led = 0
while led<30: # si cambio a led<60 al cruzarse se cambian los colores
    for rows in range(6):
        leds[led + rows*60] = (255,255,0)
        leds[59-led + rows*60] = (255,0,0)
    client.put_pixels(leds)
    time.sleep(.01)
    led = led + 1


#serpiente que recorre todo el panel de leds
led = 0
while True:                 #hacer el movimiento para siempre 
    for led in range(355):   # en que rango quiero que el movimiento ocurra 
        leds = [(255,255,255)]*360      #todo de un color
        leds[led+1] = (0,0,255)         #5 leds de color diferente
        leds[led+2] = (0,0,255)
        leds[led+3] = (0,0,255)
        leds[led+4] = (0,0,255)
        if led == 255:                  #si alcanza el final que vuelva al inicio
            led = 0
        client.put_pixels(leds)
        time.sleep(.01)
    break

#serpiente que recorre todo el panel de leds al reves
led = 0
while True:                 #hacer el movimiento para siempre 
    for led in range(0, 360, 60):   # en que rango queiro que el movimiento ocurra 
        leds = [(255,255,255)]*360      #todo de un color
        leds[355-led+1] = (0,0,255)         #5 leds de color diferente
        leds[355-led+2] = (0,0,255)
        leds[355-led+3] = (0,0,255)
        leds[355-led+4] = (0,0,255)
        if led == 255:                  #si alcanza el final que vuelva al inicio
            led = 0
        client.put_pixels(leds)
        time.sleep(.01)
    break


#va en columnas descendientes - no en filas        
led = 0
while True:                 #hacer el movimiento para siempre 
    for rows in range(6):   # en que rango queiro que el movimiento ocurra 
        leds = [(255,255,255)]*360      #todo de un color
        leds[led+1 + rows*60] = (0,0,255)
    break




#serpiente con cambios aleatorios de color, version 1
led = 0       
import random
while True:                         #do this forever:
    rand_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    for led in range(0, 360):
        leds = [(255,255,255)]*360  #white  #set everything white
        rand_color = (random.randint(rand_color[0]-50, rand_color[0]+50),random.randint(rand_color[1]-50, rand_color[1]+50),random.randint(rand_color[2]-20, rand_color[2]+20))
        leds[355-led] = rand_color       #set 5 leds another colour, incrementing position each frame
        leds[355-led+1] = rand_color
        leds[355-led+2] = rand_color
        leds[355-led+3] = rand_color
        leds[355-led+4] = rand_color
        if led == 355:              #if we reach the end go back;
            led = 0
        client.put_pixels(leds)     #place the latest frame on screen.
    time.sleep(0.01) 
    break

#serpiente con cambios aleatorios de color, version 2
led = 0    
import random
while True:                         #do this forever:
    for led in range(0, 360):
        leds = [(255,255,255)]*360  #white  #set everything white
        leds[355-led] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))      #set 5 leds another colour, incrementing position each frame
        leds[355-led+1] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        leds[355-led+2] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        leds[355-led+3] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        leds[355-led+4] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if led == 355:              #if we reach the end go back;
            led = 0
        client.put_pixels(leds)     #place the latest frame on screen.
    time.sleep(0.01)
    break

    
