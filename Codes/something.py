import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

led = 0
rand_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
while True:
    for led in range(60):
        leds = [(0,0,0)]*360                #W 
        leds[300-led] = rand_color
        leds[300-led+6] = rand_color
        leds[240-led] = rand_color
        leds[240-led+2] = rand_color
        leds[240-led+4] = rand_color
        leds[240-led+6] = rand_color
        leds[180-led] = rand_color
        leds[180-led+3] = rand_color
        leds[180-led+6] = rand_color
        leds[120-led] = rand_color
        leds[120-led+6] = rand_color
        leds[60-led] = rand_color
        leds[60-led+6] = rand_color
        
        leds[309-led] = rand_color         #E
        leds[309-led+2] = rand_color
        leds[309-led+4] = rand_color
        leds[309-led+6] = rand_color
        leds[249-led] = rand_color
        leds[189-led] = rand_color
        leds[189-led+4] = rand_color
        leds[189-led+2] = rand_color
        leds[129-led] = rand_color
        leds[69-led] = rand_color
        leds[69-led+2] = rand_color
        leds[69-led+4] = rand_color
        leds[69-led+6] = rand_color
        
        leds[318-led] = rand_color          #L
        leds[318-led+2] = rand_color
        leds[318-led+4] = rand_color
        leds[318-led+6] = rand_color
        leds[258-led] = rand_color
        leds[198-led] = rand_color
        leds[138-led] = rand_color
        leds[78-led] = rand_color

        leds[325-led+2] = rand_color        #C
        leds[325-led+4] = rand_color
        leds[265-led] = rand_color
        leds[265-led+6] = rand_color
        leds[205-led] = rand_color
        leds[145-led] = rand_color
        leds[145-led+6] = rand_color
        leds[85-led+2] = rand_color
        leds[85-led+4] = rand_color

        leds[334-led+2] = rand_color        #O
        leds[334-led+4] = rand_color
        leds[274-led] = rand_color
        leds[274-led+6] = rand_color
        leds[214-led] = rand_color
        leds[214-led+6] = rand_color 
        leds[154-led] = rand_color
        leds[154-led+6] = rand_color
        leds[94-led+2] = rand_color
        leds[94-led+4] = rand_color

        leds[343-led] = rand_color         #M
        leds[343-led+6] = rand_color
        leds[283-led] = rand_color
        leds[283-led+6] = rand_color
        leds[223-led] = rand_color
        leds[223-led+3] = rand_color
        leds[223-led+6] = rand_color
        leds[163-led] = rand_color
        leds[163-led+2] = rand_color
        leds[163-led+4] = rand_color
        leds[163-led+6] = rand_color
        leds[103-led] = rand_color
        leds[103-led+6] = rand_color

        leds[351-led] = rand_color      #E
        leds[351-led+2] = rand_color
        leds[351-led+4] = rand_color
        leds[351-led+6] = rand_color
        leds[291-led] = rand_color
        leds[231-led] = rand_color
        leds[231-led+4] = rand_color
        leds[231-led+2] = rand_color
        leds[171-led] = rand_color
        leds[111-led] = rand_color
        leds[111-led+2] = rand_color
        leds[111-led+4] = rand_color
        leds[111-led+6] = rand_color
        client.put_pixels(leds)
        time.sleep(.1)
    time.sleep(1)
    
    leds = [(0,0,0)]*360                #P
    rand_color = (random.randint(rand_color[0]-50, rand_color[0]+50),random.randint(rand_color[1]-50, rand_color[1]+50),random.randint(rand_color[2]-20, rand_color[2]+20))
    leds[309-led] = rand_color
    leds[249-led] = rand_color
    leds[189-led] = rand_color
    leds[189-led+4] = rand_color
    leds[189-led+2] = rand_color
    leds[129-led] = rand_color
    leds[129-led+6] = rand_color
    leds[69-led] = rand_color
    leds[69-led+2] = rand_color
    leds[69-led+4] = rand_color

    leds[318-led] = rand_color          #L
    leds[318-led+2] = rand_color
    leds[318-led+4] = rand_color
    leds[318-led+6] = rand_color
    leds[258-led] = rand_color
    leds[198-led] = rand_color
    leds[138-led] = rand_color
    leds[78-led] = rand_color

    leds[325-led] = rand_color           #A  
    leds[325-led+8] = rand_color
    leds[266-led] = rand_color
    leds[266-led+6] = rand_color
    leds[207-led] = rand_color
    leds[207-led+2] = rand_color
    leds[207-led+4] = rand_color
    leds[148-led] = rand_color
    leds[148-led+2] = rand_color
    leds[89-led] = rand_color

    leds[334-led+3] = rand_color        #Y
    leds[274-led+3] = rand_color
    leds[214-led+3] = rand_color
    leds[154-led+2] = rand_color
    leds[154-led+4] = rand_color
    leds[94-led] = rand_color
    leds[94-led+6] = rand_color

    leds[343-led] = rand_color          #E
    leds[343-led+2] = rand_color
    leds[343-led+4] = rand_color
    leds[343-led+6] = rand_color
    leds[283-led] = rand_color
    leds[223-led] = rand_color
    leds[223-led+4] = rand_color
    leds[223-led+2] = rand_color
    leds[163-led] = rand_color
    leds[103-led] = rand_color
    leds[103-led+2] = rand_color
    leds[103-led+4] = rand_color
    leds[103-led+6] = rand_color

    leds[351-led] = rand_color       #R
    leds[351-led+6] = rand_color
    leds[291-led] = rand_color
    leds[291-led+4] = rand_color
    leds[231-led] = rand_color
    leds[231-led+4] = rand_color
    leds[231-led+2] = rand_color
    leds[171-led] = rand_color
    leds[171-led+6] = rand_color
    leds[111-led] = rand_color
    leds[111-led+2] = rand_color
    leds[111-led+4] = rand_color
    client.put_pixels(leds)
    time.sleep(.1)
time.sleep(1)


introduction = input('''Welcome
                \n Insert your name
                ''') # \n-newline; \t- tab

led = 0
def funcA():
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
def funcB():
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
    return(introduction)
def funcC():
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

def funcD():
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
def funcE():
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
def funcF():
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
def funcG():
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
def funcH():
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
def funcI():
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
def funcJ():
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
def funcK():
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
def funcL():
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
def funcM():
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
def funcN():
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

def funcO():
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
def funcP():
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
def funcQ():
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
def funcR():
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
def funcS():
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
def funcT():
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
def funcU():
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
def funcV():
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
def funcW():
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
def funcX():
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
def funcY():
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
def funcZ():
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




##while True:
##    if introduction.isalpha() == True:
##        
##    else:
##        introduction=input("Don't try with numbers, select letters") # ask for new value

while led<60:                 #hacer el movimiento para siempre 
    for led in range(52):
        if introduction == 'A':
            funcA()
        elif introduction == 'B':
            print(funcB())
        elif introduction == 'C':
            print(funcC())
        elif introduction == 'D':
            print(funcD())
        elif introduction == 'E':
            print(funcE())
        elif introduction == 'F':
            print(funcF())
        elif introduction == 'G':
            print(funcG())
        elif introduction == 'H':
            print(funcH())
        elif introduction == 'I':
            print(funcI())
        elif introduction == 'J':
            print(funcJ())
        elif introduction == 'K':
            print(funcK())
        elif introduction == 'L':
            print(funcL())
        elif introduction == 'M':
            print(funcM())
        elif introduction == 'N':
            print(funcN())
        elif introduction == 'O':
            print(funcO())
        elif introduction == 'P':
            print(funcP())
        elif introduction == 'Q':
            print(funcQ())
        elif introduction == 'R':
            print(funcR())
        elif introduction == 'S':
            print(funcS())
        elif introduction == 'T':
            print(funcT())
        elif introduction == 'U':
            print(funcU())
        elif introduction == 'V':
            print(funcV())
        elif introduction == 'W':
            print(funcW())
        elif introduction == 'X':
            print(funcX())
        elif introduction == 'Y':
            print(funcY())
        elif introduction == 'Z':
            print(funcZ())

