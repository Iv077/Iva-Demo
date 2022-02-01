
import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


####   A   #####   
led = 0
while led<60:                 #hacer el movimiento para siempre 
    for led in range(52):   # en que rango quiero que el movimiento ocurra 
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
##    break
##
#####   B   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
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

###   C   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led+2] = (255,0,0)
        leds[351-led+4] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[291-led+6] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[171-led+6] = (255,0,0)
        leds[111-led+2] = (255,0,0)
        leds[111-led+4] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break

###   D   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led] = (255,0,0)
        leds[351-led+2] = (255,0,0)
        leds[351-led+4] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[291-led+6] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[231-led+6] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[171-led+6] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+2] = (255,0,0)
        leds[111-led+4] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break

###   E   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led] = (255,0,0)
        leds[351-led+2] = (255,0,0)
        leds[351-led+4] = (255,0,0)
        leds[351-led+6] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[231-led+4] = (255,0,0)
        leds[231-led+2] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+2] = (255,0,0)
        leds[111-led+4] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break

###   F   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[231-led+4] = (255,0,0)
        leds[231-led+2] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+2] = (255,0,0)
        leds[111-led+4] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break


###   G   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led+2] = (255,0,0)
        leds[351-led+4] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[291-led+6] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[231-led+4] = (255,0,0)
        leds[231-led+3] = (255,0,0)
        leds[231-led+5] = (255,0,0)
        leds[171-led] = (255,0,0)       
        leds[111-led+2] = (255,0,0)
        leds[111-led+3] = (255,0,0)
        leds[111-led+4] = (255,0,0)
        leds[111-led+5] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break


###   H   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led] = (255,0,0)
        leds[351-led+6] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[291-led+6] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[231-led+2] = (255,0,0)
        leds[231-led+4] = (255,0,0)
        leds[231-led+6] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[171-led+6] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break


###   I   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led] = (255,0,0)
        leds[351-led+3] = (255,0,0)
        leds[351-led+6] = (255,0,0)
        leds[291-led+3] = (255,0,0)
        leds[231-led+3] = (255,0,0)
        leds[171-led+3] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+3] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break


###   J   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led+2] = (255,0,0)
        leds[351-led+4] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[291-led+4] = (255,0,0)
        leds[231-led+4] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[171-led+4] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+2] = (255,0,0)
        leds[111-led+4] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break


###   K   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led] = (255,0,0)
        leds[351-led+6] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[291-led+5] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[231-led+2] = (255,0,0)
        leds[231-led+4] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[171-led+5] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break


###   L   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led] = (255,0,0)
        leds[351-led+2] = (255,0,0)
        leds[351-led+4] = (255,0,0)
        leds[351-led+6] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[111-led] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break


###   M   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led] = (255,0,0)
        leds[351-led+6] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[291-led+6] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[231-led+3] = (255,0,0)
        leds[231-led+6] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[171-led+2] = (255,0,0)
        leds[171-led+4] = (255,0,0)
        leds[171-led+6] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break

###   N   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led] = (255,0,0)
        leds[351-led+5] = (255,0,0)
        leds[351-led+6] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[291-led+4] = (255,0,0)
        leds[291-led+6] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[231-led+3] = (255,0,0)
        leds[231-led+6] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[171-led+2] = (255,0,0)
        leds[171-led+6] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+1] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break

###   O   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led+2] = (255,0,0)
        leds[351-led+4] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[291-led+6] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[231-led+6] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[171-led+6] = (255,0,0)
        leds[111-led+2] = (255,0,0)
        leds[111-led+4] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break


###   P   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[231-led+4] = (255,0,0)
        leds[231-led+2] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[171-led+6] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+2] = (255,0,0)
        leds[111-led+4] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break


###   Q   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led+2] = (255,0,0)
        leds[351-led+4] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[291-led+4] = (255,0,0)
        leds[291-led+6] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[231-led+6] = (255,0,0)
        leds[231-led+3] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[171-led+6] = (255,0,0)
        leds[111-led+2] = (255,0,0)
        leds[111-led+4] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break

###   R   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led] = (255,0,0)
        leds[351-led+6] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[291-led+4] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[231-led+4] = (255,0,0)
        leds[231-led+2] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[171-led+6] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+2] = (255,0,0)
        leds[111-led+4] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break



###   S   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360
        leds[351-led] = (255,0,0)
        leds[351-led+2] = (255,0,0)
        leds[351-led+4] = (255,0,0)
        leds[291-led+6] = (255,0,0)
        leds[231-led+2] = (255,0,0)
        leds[231-led+4] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[111-led+2] = (255,0,0)
        leds[111-led+4] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break


###   T   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led+3] = (255,0,0)
        leds[291-led+3] = (255,0,0)
        leds[231-led+3] = (255,0,0)
        leds[171-led+3] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+3] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break


###   U   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led+2] = (255,0,0)
        leds[351-led+4] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[291-led+6] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[231-led+6] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[171-led+6] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break

###   V   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led+3] = (255,0,0)
        leds[291-led+2] = (255,0,0)
        leds[291-led+4] = (255,0,0)
        leds[231-led+1] = (255,0,0)
        leds[231-led+5] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[171-led+6] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break


###   W   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led] = (255,0,0)
        leds[351-led+6] = (255,0,0)
        leds[291-led] = (255,0,0)
        leds[291-led+2] = (255,0,0)
        leds[291-led+4] = (255,0,0)
        leds[291-led+6] = (255,0,0)
        leds[231-led] = (255,0,0)
        leds[231-led+3] = (255,0,0)
        leds[231-led+6] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[171-led+6] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break


###   X   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led] = (255,0,0)
        leds[351-led+6] = (255,0,0)
        leds[291-led+2] = (255,0,0)
        leds[291-led+4] = (255,0,0)
        leds[231-led+3] = (255,0,0)
        leds[171-led+2] = (255,0,0)
        leds[171-led+4] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break

###   Y   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led+3] = (255,0,0)
        leds[291-led+3] = (255,0,0)
        leds[231-led+3] = (255,0,0)
        leds[171-led+2] = (255,0,0)
        leds[171-led+4] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break


####   Z   #####
led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360    
        leds[351-led] = (255,0,0)
        leds[351-led+2] = (255,0,0)
        leds[351-led+4] = (255,0,0)
        leds[351-led+6] = (255,0,0)
        leds[291-led+2] = (255,0,0)
        leds[291-led+6] = (255,0,0)
        leds[231-led+3] = (255,0,0)
        leds[171-led] = (255,0,0)
        leds[171-led+4] = (255,0,0)
        leds[111-led] = (255,0,0)
        leds[111-led+2] = (255,0,0)
        leds[111-led+4] = (255,0,0)
        leds[111-led+6] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
    break
