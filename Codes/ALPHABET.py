
import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


######   A   #####   
##led = 0
##while led<60:                 #hacer el movimiento para siempre 
##    for led in range(32):   # en que rango quiero que el movimiento ocurra 
##        leds = [(0,0,0)]*360      #todo de un color
##        leds[331-led] = (255,0,0)
##        leds[331-led+8] = (255,0,0) 
##        leds[272-led] = (255,0,0)
##        leds[272-led+6] = (255,0,0)
##        leds[213-led] = (255,0,0)
##        leds[213-led+2] = (255,0,0)
##        leds[213-led+4] = (255,0,0)
##        leds[154-led] = (255,0,0)
##        leds[154-led+2] = (255,0,0)
##        leds[95-led] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
#####   B   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led] = (255,0,0)
##        leds[351-led+2] = (255,0,0)
##        leds[351-led+4] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[291-led+6] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[231-led+4] = (255,0,0)
##        leds[231-led+3] = (255,0,0)
##        leds[231-led+2] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[171-led+6] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+2] = (255,0,0)
##        leds[111-led+4] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
#####   C   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led+2] = (255,0,0)
##        leds[351-led+4] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[291-led+6] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[171-led+6] = (255,0,0)
##        leds[111-led+2] = (255,0,0)
##        leds[111-led+4] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
#####   D   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led] = (255,0,0)
##        leds[351-led+2] = (255,0,0)
##        leds[351-led+4] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[291-led+6] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[231-led+6] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[171-led+6] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+2] = (255,0,0)
##        leds[111-led+4] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
#####   E   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led] = (255,0,0)
##        leds[351-led+2] = (255,0,0)
##        leds[351-led+4] = (255,0,0)
##        leds[351-led+6] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[231-led+4] = (255,0,0)
##        leds[231-led+2] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+2] = (255,0,0)
##        leds[111-led+4] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
#####   F   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[231-led+4] = (255,0,0)
##        leds[231-led+2] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+2] = (255,0,0)
##        leds[111-led+4] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
##
#####   G   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led+2] = (255,0,0)
##        leds[351-led+4] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[291-led+6] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[231-led+4] = (255,0,0)
##        leds[231-led+3] = (255,0,0)
##        leds[231-led+5] = (255,0,0)
##        leds[171-led] = (255,0,0)       
##        leds[111-led+2] = (255,0,0)
##        leds[111-led+3] = (255,0,0)
##        leds[111-led+4] = (255,0,0)
##        leds[111-led+5] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
##
#####   H   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led] = (255,0,0)
##        leds[351-led+6] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[291-led+6] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[231-led+2] = (255,0,0)
##        leds[231-led+4] = (255,0,0)
##        leds[231-led+6] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[171-led+6] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
##
#####   I   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led] = (255,0,0)
##        leds[351-led+3] = (255,0,0)
##        leds[351-led+6] = (255,0,0)
##        leds[291-led+3] = (255,0,0)
##        leds[231-led+3] = (255,0,0)
##        leds[171-led+3] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+3] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
##
#####   J   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led+2] = (255,0,0)
##        leds[351-led+4] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[291-led+4] = (255,0,0)
##        leds[231-led+4] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[171-led+4] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+2] = (255,0,0)
##        leds[111-led+4] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
##
#####   K   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led] = (255,0,0)
##        leds[351-led+6] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[291-led+5] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[231-led+2] = (255,0,0)
##        leds[231-led+4] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[171-led+5] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
##
#####   L   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led] = (255,0,0)
##        leds[351-led+2] = (255,0,0)
##        leds[351-led+4] = (255,0,0)
##        leds[351-led+6] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
##
#####   M   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led] = (255,0,0)
##        leds[351-led+6] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[291-led+6] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[231-led+3] = (255,0,0)
##        leds[231-led+6] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[171-led+2] = (255,0,0)
##        leds[171-led+4] = (255,0,0)
##        leds[171-led+6] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
#####   N   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led] = (255,0,0)
##        leds[351-led+5] = (255,0,0)
##        leds[351-led+6] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[291-led+4] = (255,0,0)
##        leds[291-led+6] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[231-led+3] = (255,0,0)
##        leds[231-led+6] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[171-led+2] = (255,0,0)
##        leds[171-led+6] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+1] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
#####   O   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led+2] = (255,0,0)
##        leds[351-led+4] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[291-led+6] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[231-led+6] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[171-led+6] = (255,0,0)
##        leds[111-led+2] = (255,0,0)
##        leds[111-led+4] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
##
#####   P   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[231-led+4] = (255,0,0)
##        leds[231-led+2] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[171-led+6] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+2] = (255,0,0)
##        leds[111-led+4] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
##
#####   Q   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led+2] = (255,0,0)
##        leds[351-led+4] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[291-led+4] = (255,0,0)
##        leds[291-led+6] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[231-led+6] = (255,0,0)
##        leds[231-led+3] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[171-led+6] = (255,0,0)
##        leds[111-led+2] = (255,0,0)
##        leds[111-led+4] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
#####   R   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led] = (255,0,0)
##        leds[351-led+6] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[291-led+4] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[231-led+4] = (255,0,0)
##        leds[231-led+2] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[171-led+6] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+2] = (255,0,0)
##        leds[111-led+4] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
##
##
#####   S   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360
##        leds[351-led] = (255,0,0)
##        leds[351-led+2] = (255,0,0)
##        leds[351-led+4] = (255,0,0)
##        leds[291-led+6] = (255,0,0)
##        leds[231-led+2] = (255,0,0)
##        leds[231-led+4] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[111-led+2] = (255,0,0)
##        leds[111-led+4] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
##
#####   T   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led+3] = (255,0,0)
##        leds[291-led+3] = (255,0,0)
##        leds[231-led+3] = (255,0,0)
##        leds[171-led+3] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+3] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
##
#####   U   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led+2] = (255,0,0)
##        leds[351-led+4] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[291-led+6] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[231-led+6] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[171-led+6] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
#####   V   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led+3] = (255,0,0)
##        leds[291-led+2] = (255,0,0)
##        leds[291-led+4] = (255,0,0)
##        leds[231-led+1] = (255,0,0)
##        leds[231-led+5] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[171-led+6] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
##
#####   W   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led] = (255,0,0)
##        leds[351-led+6] = (255,0,0)
##        leds[291-led] = (255,0,0)
##        leds[291-led+2] = (255,0,0)
##        leds[291-led+4] = (255,0,0)
##        leds[291-led+6] = (255,0,0)
##        leds[231-led] = (255,0,0)
##        leds[231-led+3] = (255,0,0)
##        leds[231-led+6] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[171-led+6] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
##
#####   X   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led] = (255,0,0)
##        leds[351-led+6] = (255,0,0)
##        leds[291-led+2] = (255,0,0)
##        leds[291-led+4] = (255,0,0)
##        leds[231-led+3] = (255,0,0)
##        leds[171-led+2] = (255,0,0)
##        leds[171-led+4] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
#####   Y   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led+3] = (255,0,0)
##        leds[291-led+3] = (255,0,0)
##        leds[231-led+3] = (255,0,0)
##        leds[171-led+2] = (255,0,0)
##        leds[171-led+4] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
##
##
######   Z   #####
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(0,0,0)]*360    
##        leds[351-led] = (255,0,0)
##        leds[351-led+2] = (255,0,0)
##        leds[351-led+4] = (255,0,0)
##        leds[351-led+6] = (255,0,0)
##        leds[291-led+2] = (255,0,0)
##        leds[291-led+6] = (255,0,0)
##        leds[231-led+3] = (255,0,0)
##        leds[171-led] = (255,0,0)
##        leds[171-led+4] = (255,0,0)
##        leds[111-led] = (255,0,0)
##        leds[111-led+2] = (255,0,0)
##        leds[111-led+4] = (255,0,0)
##        leds[111-led+6] = (255,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break



led = 0
while True:
    for led in range(0,1):
        leds = [(0,0,0)]*360    
        leds[240+led] = (255,0,0)
        leds[240+led+6] = (255,0,0)
        leds[180+led] = (255,0,0)
        leds[180+led+2] = (255,0,0)
        leds[180+led+4] = (255,0,0)
        leds[180+led+6] = (255,0,0)
        leds[120+led] = (255,0,0)
        leds[120+led+3] = (255,0,0)
        leds[120+led+6] = (255,0,0)  
        leds[60+led] = (255,0,0)
        leds[60+led+6] = (255,0,0)
        leds[led] = (255,0,0)
        leds[led+6] = (255,0,0)
      
        leds[250+led] = (255,0,0)
        leds[250+led+3] = (255,0,0)
        leds[250+led+6] = (255,0,0)
        leds[190+led+3] = (255,0,0)
        leds[190+led+3] = (255,0,0)
        leds[70+led+3] = (255,0,0)
        leds[10+led] = (255,0,0)
        leds[10+led+3] = (255,0,0)
        leds[10+led+6] = (255,0,0)
      
        leds[260+led] = (255,0,0)
        leds[260+led+5] = (255,0,0)
        leds[260+led+6] = (255,0,0)
        leds[200+led] = (255,0,0)
        leds[200+led+4] = (255,0,0)
        leds[200+led+6] = (255,0,0)
        leds[140+led] = (255,0,0)
        leds[140+led+3] = (255,0,0)
        leds[140+led+6] = (255,0,0)
        leds[80+led] = (255,0,0)
        leds[80+led+2] = (255,0,0)
        leds[80+led+6] = (255,0,0)
        leds[20+led] = (255,0,0)
        leds[20+led+1] = (255,0,0)
        leds[20+led+6] = (255,0,0)
        
        leds[270+led] = (255,0,0)
        leds[270+led+5] = (255,0,0)
        leds[270+led+6] = (255,0,0)
        leds[210+led] = (255,0,0)
        leds[210+led+4] = (255,0,0)
        leds[210+led+6] = (255,0,0)
        leds[150+led] = (255,0,0)
        leds[150+led+3] = (255,0,0)
        leds[150+led+6] = (255,0,0)
        leds[90+led] = (255,0,0)
        leds[90+led+2] = (255,0,0)
        leds[90+led+6] = (255,0,0)
        leds[30+led] = (255,0,0)
        leds[30+led+1] = (255,0,0)
        leds[30+led+6] = (255,0,0)
        
        leds[280+led] = (255,0,0)
        leds[280+led+2] = (255,0,0)
        leds[280+led+4] = (255,0,0)
        leds[280+led+6] = (255,0,0)
        leds[220+led] = (255,0,0)
        leds[220+led] = (255,0,0)
        leds[220+led+4] = (255,0,0)
        leds[220+led+2] = (255,0,0)
        leds[100+led] = (255,0,0)
        leds[40+led] = (255,0,0)
        leds[40+led+2] = (255,0,0)
        leds[40+led+4] = (255,0,0)
        leds[40+led+6] = (255,0,0)
       
        leds[290+led] = (255,0,0)
        leds[290+led+6] = (255,0,0)
        leds[230+led] = (255,0,0)
        leds[230+led+4] = (255,0,0)
        leds[160+led] = (255,0,0)
        leds[160+led+4] = (255,0,0)
        leds[160+led+2] = (255,0,0)
        leds[110+led] = (255,0,0)
        leds[110+led+6] = (255,0,0)
        leds[50+led] = (255,0,0)
        leds[50+led+2] = (255,0,0)
        leds[50+led+4] = (255,0,0)
        time.sleep(.1)
        client.put_pixels(leds)

