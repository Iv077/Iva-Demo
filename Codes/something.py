import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

##led = 0
##rand_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
##while True:
##    for led in range(60):
##        leds = [(0,0,0)]*360                #W 
##        leds[300-led] = rand_color
##        leds[300-led+6] = rand_color
##        leds[240-led] = rand_color
##        leds[240-led+2] = rand_color
##        leds[240-led+4] = rand_color
##        leds[240-led+6] = rand_color
##        leds[180-led] = rand_color
##        leds[180-led+3] = rand_color
##        leds[180-led+6] = rand_color
##        leds[120-led] = rand_color
##        leds[120-led+6] = rand_color
##        leds[60-led] = rand_color
##        leds[60-led+6] = rand_color
##        
##        leds[309-led] = rand_color         #E
##        leds[309-led+2] = rand_color
##        leds[309-led+4] = rand_color
##        leds[309-led+6] = rand_color
##        leds[249-led] = rand_color
##        leds[189-led] = rand_color
##        leds[189-led+4] = rand_color
##        leds[189-led+2] = rand_color
##        leds[129-led] = rand_color
##        leds[69-led] = rand_color
##        leds[69-led+2] = rand_color
##        leds[69-led+4] = rand_color
##        leds[69-led+6] = rand_color
##        
##        leds[318-led] = rand_color          #L
##        leds[318-led+2] = rand_color
##        leds[318-led+4] = rand_color
##        leds[318-led+6] = rand_color
##        leds[258-led] = rand_color
##        leds[198-led] = rand_color
##        leds[138-led] = rand_color
##        leds[78-led] = rand_color
##
##        leds[325-led+2] = rand_color        #C
##        leds[325-led+4] = rand_color
##        leds[265-led] = rand_color
##        leds[265-led+6] = rand_color
##        leds[205-led] = rand_color
##        leds[145-led] = rand_color
##        leds[145-led+6] = rand_color
##        leds[85-led+2] = rand_color
##        leds[85-led+4] = rand_color
##
##        leds[334-led+2] = rand_color        #O
##        leds[334-led+4] = rand_color
##        leds[274-led] = rand_color
##        leds[274-led+6] = rand_color
##        leds[214-led] = rand_color
##        leds[214-led+6] = rand_color 
##        leds[154-led] = rand_color
##        leds[154-led+6] = rand_color
##        leds[94-led+2] = rand_color
##        leds[94-led+4] = rand_color
##
##        leds[343-led] = rand_color         #M
##        leds[343-led+6] = rand_color
##        leds[283-led] = rand_color
##        leds[283-led+6] = rand_color
##        leds[223-led] = rand_color
##        leds[223-led+3] = rand_color
##        leds[223-led+6] = rand_color
##        leds[163-led] = rand_color
##        leds[163-led+2] = rand_color
##        leds[163-led+4] = rand_color
##        leds[163-led+6] = rand_color
##        leds[103-led] = rand_color
##        leds[103-led+6] = rand_color
##
##        leds[351-led] = rand_color      #E
##        leds[351-led+2] = rand_color
##        leds[351-led+4] = rand_color
##        leds[351-led+6] = rand_color
##        leds[291-led] = rand_color
##        leds[231-led] = rand_color
##        leds[231-led+4] = rand_color
##        leds[231-led+2] = rand_color
##        leds[171-led] = rand_color
##        leds[111-led] = rand_color
##        leds[111-led+2] = rand_color
##        leds[111-led+4] = rand_color
##        leds[111-led+6] = rand_color
##        client.put_pixels(leds)
##        time.sleep(.1)
##    time.sleep(1)
##    break
##
##led = 0
##while led<60:
##    for led in range(60):  
##        leds = [(0,0,0)]*360                #P
##        rand_color = (random.randint(rand_color[0]-50, rand_color[0]+50),random.randint(rand_color[1]-50, rand_color[1]+50),random.randint(rand_color[2]-20, rand_color[2]+20))
##        leds[309-led] = rand_color
##        leds[249-led] = rand_color
##        leds[189-led] = rand_color
##        leds[189-led+4] = rand_color
##        leds[189-led+2] = rand_color
##        leds[129-led] = rand_color
##        leds[129-led+6] = rand_color
##        leds[69-led] = rand_color
##        leds[69-led+2] = rand_color
##        leds[69-led+4] = rand_color
##
##        leds[318-led] = rand_color          #L
##        leds[318-led+2] = rand_color
##        leds[318-led+4] = rand_color
##        leds[318-led+6] = rand_color
##        leds[258-led] = rand_color
##        leds[198-led] = rand_color
##        leds[138-led] = rand_color
##        leds[78-led] = rand_color
##
##        leds[325-led] = rand_color           #A  
##        leds[325-led+8] = rand_color
##        leds[266-led] = rand_color
##        leds[266-led+6] = rand_color
##        leds[207-led] = rand_color
##        leds[207-led+2] = rand_color
##        leds[207-led+4] = rand_color
##        leds[148-led] = rand_color
##        leds[148-led+2] = rand_color
##        leds[89-led] = rand_color
##
##        leds[334-led+3] = rand_color        #Y
##        leds[274-led+3] = rand_color
##        leds[214-led+3] = rand_color
##        leds[154-led+2] = rand_color
##        leds[154-led+4] = rand_color
##        leds[94-led] = rand_color
##        leds[94-led+6] = rand_color
##
##        leds[343-led] = rand_color          #E
##        leds[343-led+2] = rand_color
##        leds[343-led+4] = rand_color
##        leds[343-led+6] = rand_color
##        leds[283-led] = rand_color
##        leds[223-led] = rand_color
##        leds[223-led+4] = rand_color
##        leds[223-led+2] = rand_color
##        leds[163-led] = rand_color
##        leds[103-led] = rand_color
##        leds[103-led+2] = rand_color
##        leds[103-led+4] = rand_color
##        leds[103-led+6] = rand_color
##
##        leds[351-led] = rand_color       #R
##        leds[351-led+6] = rand_color
##        leds[291-led] = rand_color
##        leds[291-led+4] = rand_color
##        leds[231-led] = rand_color
##        leds[231-led+4] = rand_color
##        leds[231-led+2] = rand_color
##        leds[171-led] = rand_color
##        leds[171-led+6] = rand_color
##        leds[111-led] = rand_color
##        leds[111-led+2] = rand_color
##        leds[111-led+4] = rand_color
##        client.put_pixels(leds)
##        time.sleep(.1)
##    time.sleep(1)
##    break

value = input('''FROM THIS MOMENT YOU ARE GOING TO PLAY AGAINST 'THE PANEL' TO
                    \n AN INCREDIBLE DANGEROUS GAME:
              
                    \n NOW CHOOSE YOUR WEAPON:

                    \t 1. ROCK
                    \t 2. PAPER
                    \t 3. SCISSORS
                    \t 4. LIZARD
                    \t 5. SPOKE 
                Type the number of yout choise and press enter.''') # \n-newline; \t- tab
led=0
def func1():
    for rows in range(6):
##    for led in range(360):
        leds =[(0,0,0)]*360
        leds[led+62] = (175,75,0)
        leds[led+63] = (175,75,0)
        leds[led+64] = (175,75,0)
        leds[led+65] = (200,150,100)
        leds[led+66] = (200,150,100)
        leds[led+67] = (200,150,100)
        leds[led+68] = (200,150,100)
        leds[led+69] = (200,150,100)
        leds[led+70] = (200,150,100)
        leds[led+71] = (200,150,100)        
        leds[led+4] = (175,75,0)
        leds[led+5] = (175,75,0)
        leds[led+6] = (175,75,0)
        leds[led+7] = (200,150,100)
        leds[led+8] = (200,150,100)
        leds[led+9] = (200,150,100)        
        leds[led+121] = (175,75,0)
        leds[led+122] = (175,75,0)
        leds[led+123] = (175,75,0)
        leds[led+124] = (200,150,100)
        leds[led+125] = (200,150,100)
        leds[led+126] = (200,150,100)
        leds[led+127] = (200,150,100)
        leds[led+128] = (200,150,100)        
        leds[led+129] = (200,150,100)
        leds[led+130] = (200,150,100)
        leds[led+131] = (200,150,100)
        leds[led+132] = (200,150,100)    
        leds[led+181] = (175,75,0)       
        leds[led+182] = (175,75,0)  
        leds[led+183] = (175,75,0)  
        leds[led+184] = (200,150,100)   
        leds[led+185] = (200,150,100)
        leds[led+186] = (200,150,100)
        leds[led+187] = (200,150,100)
        leds[led+188] = (200,150,100)
        leds[led+189] = (200,150,100)
        leds[led+190] = (200,150,100)
        leds[led+191] = (200,150,100)
        leds[led+192] = (200,150,100)        
        leds[led+242] = (175,75,0)
        leds[led+243] = (175,75,0)
        leds[led+244] = (175,75,0)
        leds[led+245] = (200,150,100)
        leds[led+246] = (200,150,100)
        leds[led+247] = (200,150,100)
        leds[led+248] = (200,150,100)
        leds[led+249] = (200,150,100)
        leds[led+250] = (200,150,100)
        leds[led+251] = (200,150,100)        
        leds[led+304] = (175,75,0)
        leds[led+305] = (175,75,0)
        leds[led+306] = (175,75,0)
        leds[led+307] = (200,150,100)
        leds[led+308] = (200,150,100)
        leds[led+309] = (200,150,100)
        client.put_pixels(leds)
        time.sleep(.1)
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
    func1()
elif value == 2:
    print(func2(value))
elif value == 3:
    print(func3(value))
elif value == 4:
    print(func4(value))
elif value == 5:
    print(func5(value))

