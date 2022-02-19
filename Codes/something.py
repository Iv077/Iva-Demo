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
    break

led = 0
while led<60:
    for led in range(60):  
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
    break

value = input('''FROM THIS MOMENT YOU ARE GOING TO PLAY AGAINST 'THE PANEL' TO
                    \n AN INCREDIBLE DANGEROUS GAME:
              
                    \n NOW CHOOSE YOUR WEAPON:

                    \n 1. ROCK
                    \n 2. PAPER
                    \n 3. SCISSORS
                    \n 4. LIZARD
                    \n 5. SPOKE 
                ''') # \n-newline; \t- tab

def func1(val):
    return val**val;
def func2(val):
    return val**val;
def func3(val):
    return val**val;
def func4(val):
    return val**val;
def func5(val):
    return val**val;

while True:
    if value.isdigit() == True: #.isgigit()
        value = int(value)
        if value > 5 or value < 1: #if value is outside our range:
            value = input("That option is not possible, try a number between 1 and 5")
            continue #skip rest of loop, start from isdigit() check again.
        else:
            break # on correct value datatype: exit the loop
    else:
        value=input("Don't try with letters, select a number:") # ask for new value

if value == 1:
    print(func1(value))
elif value == 2:
    print(func2(value))
elif value == 3:
    print(func3(value))
elif value == 4:
    print(func4(value))
elif value == 5:
    print(func5(value))

