
import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

####introduction = input('''Welcome
####                \n Insert your name
####                ''') # \n-newline; \t- tab
####
##led = 0
##while led<30: # si cambio a led<60 al cruzarse se cambian los colores
##    for rows in range(6):
##        leds[led + rows*60] = (255,255,0)
##        leds[59-led + rows*60] = (255,0,255)
##    client.put_pixels(leds)
##    time.sleep(.1)
##    led = led + 1
##led = 0
##while led<30:
##    for rows in range(1,5):
##        leds[29+led + rows*60] = (0,0,0)
##        leds[30-led + rows*60] = (0,0,0)
##    client.put_pixels(leds)
##    time.sleep(.1)
##    led = led + 1


    
##led = 0
##while led<60:                 
##    for led in range(52):   
##        leds = [(255,255,255)]*360    
##        leds[351-led] = (0,0,0)
##        leds[351-led+5] = (0,0,0)
##        leds[351-led+6] = (0,0,0)
##        leds[291-led] = (0,0,0)
##        leds[291-led+4] = (0,0,0)
##        leds[291-led+6] = (0,0,0)
##        leds[231-led] = (0,0,0)
##        leds[231-led+3] = (0,0,0)
##        leds[231-led+6] = (0,0,0)
##        leds[171-led] = (0,0,0)
##        leds[171-led+2] = (0,0,0)
##        leds[171-led+6] = (0,0,0)
##        leds[111-led] = (0,0,0)
##        leds[111-led+1] = (0,0,0)
##        leds[111-led+6] = (0,0,0)
##        
##        leds[351-led] = (0,0,0)
##        leds[351-led+2] = (0,0,0)
##        leds[351-led+4] = (0,0,0)
##        leds[351-led+6] = (0,0,0)
##        leds[291-led] = (0,0,0)
##        leds[231-led] = (0,0,0)
##        leds[231-led+4] = (0,0,0)
##        leds[231-led+2] = (0,0,0)
##        leds[171-led] = (0,0,0)
##        leds[111-led] = (0,0,0)
##        leds[111-led+2] = (0,0,0)
##        leds[111-led+4] = (0,0,0)
##        leds[111-led+6] = (0,0,0)   
##        leds[351-led] = (0,0,0)
##        leds[351-led+6] = (0,0,0)
##        leds[291-led] = (0,0,0)
##        leds[291-led+2] = (0,0,0)
##        leds[291-led+4] = (0,0,0)
##        leds[291-led+6] = (0,0,0)
##        leds[231-led] = (0,0,0)
##        leds[231-led+3] = (0,0,0)
##        leds[231-led+6] = (0,0,0)
##        leds[171-led] = (0,0,0)
##        leds[171-led+6] = (0,0,0)
##        leds[111-led] = (0,0,0)
##        leds[111-led+6] = (0,0,0)
##        client.put_pixels(leds)
##        time.sleep(.1)
##        break
    
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




while True:
    if introduction.isalpha() == False:
        introduction=input("Don't try with numbers, select letters") # ask for new value

while led<60:                 #hacer el movimiento para siempre 
    for led in range(52):
        if introduction == 'A':
            print(funcA())
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



