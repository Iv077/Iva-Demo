import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

##led = 0
rand_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
##while True:
##    for led in range(60):
##        leds = [(0,0,0)]*360                #W 
##        leds[300-led] = (255,0,0)
##        leds[300-led+6] = (255,0,0)
##        leds[240-led] = (255,0,0)
##        leds[240-led+2] = (255,0,0)
##        leds[240-led+4] = (255,0,0)
##        leds[240-led+6] = (255,0,0)
##        leds[180-led] = (255,0,0)
##        leds[180-led+3] = (255,0,0)
##        leds[180-led+6] = (255,0,0)
##        leds[120-led] = (255,0,0)
##        leds[120-led+6] = (255,0,0)
##        leds[60-led] = (255,0,0)
##        leds[60-led+6] = (255,0,0)
##        
##        leds[309-led] = (255,128,0)         #E
##        leds[309-led+2] = (255,128,0)
##        leds[309-led+4] = (255,128,0)
##        leds[309-led+6] = (255,128,0)
##        leds[249-led] = (255,128,0)
##        leds[189-led] = (255,128,0)
##        leds[189-led+4] = (255,128,0)
##        leds[189-led+2] = (255,128,0)
##        leds[129-led] = (255,128,0)
##        leds[69-led] = (255,128,0)
##        leds[69-led+2] = (255,128,0)
##        leds[69-led+4] = (255,128,0)
##        leds[69-led+6] = (255,128,0)
##        
##        leds[318-led] = (255,255,0)         #L
##        leds[318-led+2] = (255,255,0)
##        leds[318-led+4] = (255,255,0)
##        leds[318-led+6] = (255,255,0)
##        leds[258-led] = (255,255,0)
##        leds[198-led] = (255,255,0)
##        leds[138-led] = (255,255,0)
##        leds[78-led] = (255,255,0)
##
##        leds[325-led+2] = (0,255,0)        #C
##        leds[325-led+4] = (0,255,0) 
##        leds[265-led] = (0,255,0) 
##        leds[265-led+6] = (0,255,0) 
##        leds[205-led] = (0,255,0) 
##        leds[145-led] = (0,255,0) 
##        leds[145-led+6] = (0,255,0) 
##        leds[85-led+2] = (0,255,0) 
##        leds[85-led+4] = (0,255,0) 
##
##        leds[334-led+2] = (0,255,255)        #O
##        leds[334-led+4] = (0,255,255)
##        leds[274-led] = (0,255,255)
##        leds[274-led+6] = (0,255,255)
##        leds[214-led] = (0,255,255)
##        leds[214-led+6] = (0,255,255) 
##        leds[154-led] = (0,255,255)
##        leds[154-led+6] = (0,255,255)
##        leds[94-led+2] = (0,255,255)
##        leds[94-led+4] = (0,255,255)
##
##        leds[343-led] = (0,0,255)         #M
##        leds[343-led+6] = (0,0,255)
##        leds[283-led] = (0,0,255)
##        leds[283-led+6] = (0,0,255)
##        leds[223-led] = (0,0,255)
##        leds[223-led+3] = (0,0,255)
##        leds[223-led+6] = (0,0,255)
##        leds[163-led] = (0,0,255)
##        leds[163-led+2] = (0,0,255)
##        leds[163-led+4] = (0,0,255)
##        leds[163-led+6] = (0,0,255)
##        leds[103-led] = (0,0,255)
##        leds[103-led+6] = (0,0,255)
##
##        leds[351-led] = (255,0,255)      #E
##        leds[351-led+2] = (255,0,255)
##        leds[351-led+4] = (255,0,255)
##        leds[351-led+6] = (255,0,255)
##        leds[291-led] = (255,0,255)
##        leds[231-led] = (255,0,255)
##        leds[231-led+4] = (255,0,255)
##        leds[231-led+2] = (255,0,255)
##        leds[171-led] = (255,0,255)
##        leds[111-led] = (255,0,255)
##        leds[111-led+2] = (255,0,255)
##        leds[111-led+4] = (255,0,255)
##        leds[111-led+6] = (255,0,255)
##        client.put_pixels(leds)
##        time.sleep(.05)
##    time.sleep(0.5)
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
##        time.sleep(.05)
##    time.sleep(1)
##    break

panel_weapon_list = [6, 7, 8, 9, 10]

panel_choice = random.choice(panel_weapon_list)



value = input('''FROM THIS MOMENT YOU ARE GOING TO PLAY AGAINST 'THE PANEL' TO
            \n   AN INCREDIBLE DANGEROUS GAME
              
                    \n NOW CHOOSE YOUR WEAPON:

                    \t 1. ROCK
                    \t 2. PAPER
                    \t 3. SCISSORS
                    \t 4. LIZARD
                    \t 5. SPOKE
                    
                Type the number of yout choise and press enter.''') # \n-newline; \t- tab

#VS#
led=0
def func0():
    for led in range(24,25):   
        leds = [(0,0,0)]*360    
        leds[344-led+3] = rand_color
        leds[284-led+2] = rand_color
        leds[284-led+4] = rand_color
        leds[224-led+1] = rand_color
        leds[224-led+5] = rand_color
        leds[164-led] = rand_color
        leds[164-led+6] = rand_color
        leds[104-led] = rand_color
        leds[104-led+6] = rand_color    
        leds[351-led] = rand_color
        leds[351-led+2] = rand_color
        leds[351-led+4] = rand_color
        leds[291-led+6] = rand_color
        leds[231-led+2] = rand_color
        leds[231-led+4] = rand_color
        leds[171-led] = rand_color
        leds[111-led+2] = rand_color
        leds[111-led+4] = rand_color
        leds[111-led+6] = rand_color
        client.put_pixels(leds)
        time.sleep(.1)
    time.sleep(4)


#ROCK#
def func1():
    for led in range(0,10):
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
        
#PAPER#
def func2():
    for led in range(0,10):   
        leds =[(0,0,0)]*360     
        leds[led+1] = (255,255,255)        
        leds[led+2] = (255,255,255)
        leds[led+3] = (255,255,255)
        leds[led+4] = (255,255,255)
        leds[led+5] = (255,255,255)
        leds[led+6] = (255,255,255)
        leds[led+7] = (255,255,255)
        leds[led+8] = (255,255,255)
        leds[led+61] = (255,255,255)
        leds[led+62] = (255,255,255)
        leds[led+63] = (255,255,255)
        leds[led+64] = (255,255,255)
        leds[led+65] = (255,255,255)
        leds[led+66] = (255,255,255)
        leds[led+67] = (255,255,255)
        leds[led+68] = (255,255,255)
        leds[led+121] = (255,255,255)
        leds[led+122] = (255,255,255)
        leds[led+123] = (255,255,255)
        leds[led+125] = (255,255,255)
        leds[led+126] = (255,255,255)
        leds[led+127] = (255,255,255)
        leds[led+128] = (255,255,255)
        leds[led+129] = (255,255,255)
        leds[led+130] = (255,255,255)
        leds[led+131] = (255,255,255)
        leds[led+132] = (255,255,255)
        leds[led+181] = (255,255,255)
        leds[led+182] = (255,255,255)
        leds[led+183] = (255,255,255)
        leds[led+185] = (255,255,255)
        leds[led+186] = (255,255,255)
        leds[led+187] = (255,255,255)
        leds[led+188] = (255,255,255)
        leds[led+189] = (255,255,255)
        leds[led+190] = (255,255,255)
        leds[led+191] = (255,255,255)
        leds[led+192] = (255,255,255)
        leds[led+245] = (255,255,255)
        leds[led+246] = (255,255,255)
        leds[led+247] = (255,255,255)
        leds[led+248] = (255,255,255)
        leds[led+249] = (255,255,255)
        leds[led+250] = (255,255,255)
        leds[led+251] = (255,255,255)
        leds[led+252] = (255,255,255)
        leds[led+305] = (255,255,255)
        leds[led+306] = (255,255,255)
        leds[led+307] = (255,255,255)
        leds[led+308] = (255,255,255)
        leds[led+309] = (255,255,255)
        leds[led+310] = (255,255,255)
        leds[led+311] = (255,255,255)
        leds[led+312] = (255,255,255)
        client.put_pixels(leds)
        time.sleep(.1)

#SCISSORS#
def func3():
    for led in range(0,10): 
        leds =[(0,0,0)]*360
        leds[led+1] = (255,0,0)        
        leds[led+2] = (255,0,0)
        leds[led+3] = (255,0,0)
        leds[led+4] = (255,0,0) 
        leds[led+5] = (255,0,0) 
        leds[led+60] = (255,0,0)
        leds[led+66] = (255,0,0)
        leds[led+121] = (255,0,0)
        leds[led+122] = (255,0,0)
        leds[led+123] = (255,0,0) 
        leds[led+124] = (255,0,0) 
        leds[led+125] = (255,0,0)
        leds[led+181] = (255,0,0)        
        leds[led+182] = (255,0,0)
        leds[led+183] = (255,0,0)
        leds[led+184] = (255,0,0) 
        leds[led+185] = (255,0,0)
        leds[led+240] = (255,0,0)
        leds[led+246] = (255,0,0)
        leds[led+301] = (255,0,0)
        leds[led+302] = (255,0,0)
        leds[led+303] = (255,0,0)
        leds[led+304] = (255,0,0)
        leds[led+305] = (255,0,0)
        leds[led+127] = (255,255,255)
        leds[led+187] = (255,255,255)
        leds[led+128] = (150,150,150)
        leds[led+129] = (150,150,150)
        leds[led+189] = (150,150,150)        
        leds[led+188] = (150,150,150)        
        leds[led+69] = (150,150,150)
        leds[led+70] = (150,150,150)
        leds[led+71] = (150,150,150)
        leds[led+11] = (150,150,150)        
        leds[led+12] = (150,150,150)
        leds[led+13] = (150,150,150)        
        leds[led+249] = (150,150,150)
        leds[led+250] = (150,150,150)
        leds[led+251] = (150,150,150)
        leds[led+311] = (150,150,150)
        leds[led+312] = (150,150,150)
        leds[led+313] = (150,150,150)
        client.put_pixels(leds)
        time.sleep(.1)

#LIZARD#
def func4():
    for led in range(0,10):
        leds =[(0,0,0)]*360
        leds[led+61] = (255,255,0)        
        leds[led+62] = (255,0,0)
        leds[led+63] = (255,255,0)
        leds[led+64] = (0,100,0)
        leds[led+65] = (0,255,0)
        leds[led+66] = (0,255,0)
        leds[led+67] = (0,255,0)
        leds[led+68] = (0,255,0)
        leds[led+69] = (0,100,0)
        leds[led+70] = (255,255,0)
        leds[led+71] = (255,0,0)
        leds[led+72] = (255,255,0)                
        leds[led+4] = (0,255,0)
        leds[led+5] = (0,255,0)
        leds[led+6] = (0,255,0)
        leds[led+7] = (0,255,0)
        leds[led+8] = (0,255,0)
        leds[led+9] = (0,255,0)
        leds[led+120] = (255,255,0)
        leds[led+121] = (255,255,0)
        leds[led+122] = (255,0,0)
        leds[led+123] = (255,255,0)
        leds[led+124] = (255,255,0)
        leds[led+125] = (0,100,0)
        leds[led+126] = (150,150,150)
        leds[led+127] = (150,150,150)
        leds[led+128] = (0,100,0)        
        leds[led+129] = (255,255,0)
        leds[led+130] = (255,255,0)
        leds[led+131] = (255,0,0)
        leds[led+132] = (255,255,0)
        leds[led+133] = (255,255,0)                
        leds[led+181] = (255,255,0)       
        leds[led+182] = (255,0,0) 
        leds[led+183] = (255,255,0) 
        leds[led+184] = (0,100,0)  
        leds[led+185] = (150,150,150)
        leds[led+186] = (150,150,150)
        leds[led+187] = (150,150,150)
        leds[led+188] = (150,150,150)
        leds[led+189] = (0,100,0)
        leds[led+190] = (255,255,0)
        leds[led+191] = (255,0,0)
        leds[led+192] = (255,255,0)       
        leds[led+242] = (0,100,0)
        leds[led+243] = (0,100,0)
        leds[led+244] = (0,255,0)
        leds[led+245] = (0,255,0)
        leds[led+246] = (255,0,255)
        leds[led+247] = (255,0,255)
        leds[led+248] = (0,255,0)
        leds[led+249] = (0,255,0)
        leds[led+250] = (0,100,0)
        leds[led+251] = (0,100,0)        
        leds[led+304] = (0,255,0)
        leds[led+305] = (0,255,0)
        leds[led+306] = (0,255,0)
        leds[led+307] = (255,0,255)
        leds[led+308] = (255,0,255)
        leds[led+309] = (255,0,255)        
        client.put_pixels(leds)
        time.sleep(.1)

#SPOK#
def func5():
    for led in range(0,10):
        leds =[(0,0,0)]*360 
        leds[led+64] = (255,218,185)
        leds[led+65] = (255,218,185)
        leds[led+66] = (255,218,185)
        leds[led+68] = (255,218,185)
        leds[led+69] = (255,218,185)
        leds[led+70] = (255,218,185)
        leds[led+4] = (255,218,185)
        leds[led+5] = (255,218,185)
        leds[led+9] = (255,218,185)
        leds[led+10] = (255,218,185)        
        leds[led+121] = (255,218,185)
        leds[led+122] = (255,218,185)
        leds[led+124] = (255,218,185)
        leds[led+125] = (255,218,185)
        leds[led+126] = (255,218,185)
        leds[led+127] = (255,218,185)
        leds[led+128] = (255,218,185)       
        leds[led+129] = (255,218,185)
        leds[led+130] = (255,218,185)
        leds[led+182] = (255,218,185) 
        leds[led+183] = (255,218,185)
        leds[led+184] = (255,218,185)  
        leds[led+185] = (255,218,185)
        leds[led+186] = (255,218,185)
        leds[led+187] = (255,218,185)
        leds[led+188] = (255,218,185)
        leds[led+189] = (255,218,185)
        leds[led+190] = (255,218,185)       
        leds[led+243] = (255,218,185)
        leds[led+244] = (255,218,185)
        leds[led+245] = (255,218,185)
        leds[led+246] = (255,218,185)
        leds[led+247] = (255,218,185)
        leds[led+248] = (255,218,185)
        leds[led+249] = (255,218,185)
        leds[led+250] = (255,218,185)
        leds[led+305] = (255,218,185)
        leds[led+306] = (255,218,185)
        leds[led+307] = (255,218,185)
        leds[led+308] = (255,218,185)
        client.put_pixels(leds)
        time.sleep(.1)

#ROCK#
def func6():
    for led in range(2,10):
        leds =[(0,0,0)]*360     #si ponemos 48- se mueve de derrecha a izqueirD, si lo quitamos se mueve de izqueirda a derrecha
        leds[48-led+62] = (175,75,0)
        leds[48-led+63] = (175,75,0)
        leds[48-led+64] = (175,75,0)
        leds[48-led+65] = (200,150,100)
        leds[48-led+66] = (200,150,100)
        leds[48-led+67] = (200,150,100)
        leds[48-led+68] = (200,150,100)
        leds[48-led+69] = (200,150,100)
        leds[48-led+70] = (200,150,100)
        leds[48-led+71] = (200,150,100)        
        leds[48-led+4] = (175,75,0)
        leds[48-led+5] = (175,75,0)
        leds[48-led+6] = (175,75,0)
        leds[48-led+7] = (200,150,100)
        leds[48-led+8] = (200,150,100)
        leds[48-led+9] = (200,150,100)        
        leds[48-led+121] = (175,75,0)
        leds[48-led+122] = (175,75,0)
        leds[48-led+123] = (175,75,0)
        leds[48-led+124] = (200,150,100)
        leds[48-led+125] = (200,150,100)
        leds[48-led+126] = (200,150,100)
        leds[48-led+127] = (200,150,100)
        leds[48-led+128] = (200,150,100)        
        leds[48-led+129] = (200,150,100)
        leds[48-led+130] = (200,150,100)
        leds[48-led+131] = (200,150,100)
        leds[48-led+132] = (200,150,100)    
        leds[48-led+181] = (175,75,0)       
        leds[48-led+182] = (175,75,0)  
        leds[48-led+183] = (175,75,0)  
        leds[48-led+184] = (200,150,100)   
        leds[48-led+185] = (200,150,100)
        leds[48-led+186] = (200,150,100)
        leds[48-led+187] = (200,150,100)
        leds[48-led+188] = (200,150,100)
        leds[48-led+189] = (200,150,100)
        leds[48-led+190] = (200,150,100)
        leds[48-led+191] = (200,150,100)
        leds[48-led+192] = (200,150,100)        
        leds[48-led+242] = (175,75,0)
        leds[48-led+243] = (175,75,0)
        leds[48-led+244] = (175,75,0)
        leds[48-led+245] = (200,150,100)
        leds[48-led+246] = (200,150,100)
        leds[48-led+247] = (200,150,100)
        leds[48-led+248] = (200,150,100)
        leds[48-led+249] = (200,150,100)
        leds[48-led+250] = (200,150,100)
        leds[48-led+251] = (200,150,100)        
        leds[48-led+304] = (175,75,0)
        leds[48-led+305] = (175,75,0)
        leds[48-led+306] = (175,75,0)
        leds[48-led+307] = (200,150,100)
        leds[48-led+308] = (200,150,100)
        leds[48-led+309] = (200,150,100)
        client.put_pixels(leds)
        time.sleep(0.1)

#PAPER#
def func7():
    for led in range(2,10):
        leds =[(0,0,0)]*360     
        leds[48-led+1] = (255,255,255)        
        leds[48-led+2] = (255,255,255)
        leds[48-led+3] = (255,255,255)
        leds[48-led+4] = (255,255,255)
        leds[48-led+5] = (255,255,255)
        leds[48-led+6] = (255,255,255)
        leds[48-led+7] = (255,255,255)
        leds[48-led+8] = (255,255,255)
        leds[48-led+61] = (255,255,255)
        leds[48-led+62] = (255,255,255)
        leds[48-led+63] = (255,255,255)
        leds[48-led+64] = (255,255,255)
        leds[48-led+65] = (255,255,255)
        leds[48-led+66] = (255,255,255)
        leds[48-led+67] = (255,255,255)
        leds[48-led+68] = (255,255,255)
        leds[48-led+121] = (255,255,255)
        leds[48-led+122] = (255,255,255)
        leds[48-led+123] = (255,255,255)
        leds[48-led+125] = (255,255,255)
        leds[48-led+126] = (255,255,255)
        leds[48-led+127] = (255,255,255)
        leds[48-led+128] = (255,255,255)
        leds[48-led+129] = (255,255,255)
        leds[48-led+130] = (255,255,255)
        leds[48-led+131] = (255,255,255)
        leds[48-led+132] = (255,255,255)
        leds[48-led+181] = (255,255,255)
        leds[48-led+182] = (255,255,255)
        leds[48-led+183] = (255,255,255)
        leds[48-led+185] = (255,255,255)
        leds[48-led+186] = (255,255,255)
        leds[48-led+187] = (255,255,255)
        leds[48-led+188] = (255,255,255)
        leds[48-led+189] = (255,255,255)
        leds[48-led+190] = (255,255,255)
        leds[48-led+191] = (255,255,255)
        leds[48-led+192] = (255,255,255)
        leds[48-led+245] = (255,255,255)
        leds[48-led+246] = (255,255,255)
        leds[48-led+247] = (255,255,255)
        leds[48-led+248] = (255,255,255)
        leds[48-led+249] = (255,255,255)
        leds[48-led+250] = (255,255,255)
        leds[48-led+251] = (255,255,255)
        leds[48-led+252] = (255,255,255)
        leds[48-led+305] = (255,255,255)
        leds[48-led+306] = (255,255,255)
        leds[48-led+307] = (255,255,255)
        leds[48-led+308] = (255,255,255)
        leds[48-led+309] = (255,255,255)
        leds[48-led+310] = (255,255,255)
        leds[48-led+311] = (255,255,255)
        leds[48-led+312] = (255,255,255)
        client.put_pixels(leds)
        time.sleep(.1)

#SCISSORS#
def func8():
    for led in range(2,10):
        leds =[(0,0,0)]*360
        leds[48-led+1] = (255,0,0)        
        leds[48-led+2] = (255,0,0)
        leds[48-led+3] = (255,0,0)
        leds[48-led+4] = (255,0,0) 
        leds[48-led+5] = (255,0,0) 
        leds[48-led+60] = (255,0,0)
        leds[48-led+66] = (255,0,0)
        leds[48-led+121] = (255,0,0)
        leds[48-led+122] = (255,0,0)
        leds[48-led+123] = (255,0,0) 
        leds[48-led+124] = (255,0,0) 
        leds[48-led+125] = (255,0,0)
        leds[48-led+181] = (255,0,0)        
        leds[48-led+182] = (255,0,0)
        leds[48-led+183] = (255,0,0)
        leds[48-led+184] = (255,0,0) 
        leds[48-led+185] = (255,0,0)
        leds[48-led+240] = (255,0,0)
        leds[48-led+246] = (255,0,0)
        leds[48-led+301] = (255,0,0)
        leds[48-led+302] = (255,0,0)
        leds[48-led+303] = (255,0,0)
        leds[48-led+304] = (255,0,0)
        leds[48-led+305] = (255,0,0)
        leds[48-led+127] = (255,255,255)
        leds[48-led+187] = (255,255,255)
        leds[48-led+128] = (150,150,150)
        leds[48-led+129] = (150,150,150)
        leds[48-led+189] = (150,150,150)        
        leds[48-led+188] = (150,150,150)        
        leds[48-led+69] = (150,150,150)
        leds[48-led+70] = (150,150,150)
        leds[48-led+71] = (150,150,150)
        leds[48-led+11] = (150,150,150)        
        leds[48-led+12] = (150,150,150)
        leds[48-led+13] = (150,150,150)        
        leds[48-led+249] = (150,150,150)
        leds[48-led+250] = (150,150,150)
        leds[48-led+251] = (150,150,150)
        leds[48-led+311] = (150,150,150)
        leds[48-led+312] = (150,150,150)
        leds[48-led+313] = (150,150,150)
        client.put_pixels(leds)
        time.sleep(.1)

#LIZARD#
def func9():
    for led in range(2,10):
        leds =[(0,0,0)]*360
        leds[48-led+61] = (255,255,0)        
        leds[48-led+62] = (255,0,0)
        leds[48-led+63] = (255,255,0)
        leds[48-led+64] = (0,100,0)
        leds[48-led+65] = (0,255,0)
        leds[48-led+66] = (0,255,0)
        leds[48-48-led+67] = (0,255,0)
        leds[48-led+68] = (0,255,0)
        leds[48-led+69] = (0,100,0)
        leds[48-led+70] = (255,255,0)
        leds[48-led+71] = (255,0,0)
        leds[48-led+72] = (255,255,0)                
        leds[48-led+4] = (0,255,0)
        leds[48-led+5] = (0,255,0)
        leds[48-led+6] = (0,255,0)
        leds[48-led+7] = (0,255,0)
        leds[48-led+8] = (0,255,0)
        leds[48-led+9] = (0,255,0)
        leds[48-led+120] = (255,255,0)
        leds[48-led+121] = (255,255,0)
        leds[48-led+122] = (255,0,0)
        leds[48-led+123] = (255,255,0)
        leds[48-led+124] = (255,255,0)
        leds[48-led+125] = (0,100,0)
        leds[48-led+126] = (150,150,150)
        leds[48-led+127] = (150,150,150)
        leds[48-led+128] = (0,100,0)        
        leds[48-led+129] = (255,255,0)
        leds[48-led+130] = (255,255,0)
        leds[48-led+131] = (255,0,0)
        leds[48-led+132] = (255,255,0)
        leds[48-led+133] = (255,255,0)                
        leds[48-led+181] = (255,255,0)       
        leds[48-led+182] = (255,0,0) 
        leds[48-led+183] = (255,255,0) 
        leds[48-led+184] = (0,100,0)  
        leds[48-led+185] = (150,150,150)
        leds[48-led+186] = (150,150,150)
        leds[48-led+187] = (150,150,150)
        leds[48-led+188] = (150,150,150)
        leds[48-led+189] = (0,100,0)
        leds[48-led+190] = (255,255,0)
        leds[48-led+191] = (255,0,0)
        leds[48-led+192] = (255,255,0)        
        leds[48-led+242] = (0,100,0)
        leds[48-led+243] = (0,100,0)
        leds[48-led+244] = (0,255,0)
        leds[48-led+245] = (0,255,0)
        leds[48-led+246] = (255,0,255)
        leds[48-led+247] = (255,0,255)
        leds[48-led+248] = (0,255,0)
        leds[48-led+249] = (0,255,0)
        leds[48-led+250] = (0,100,0)
        leds[48-led+251] = (0,100,0)        
        leds[48-led+304] = (0,255,0)
        leds[48-led+305] = (0,255,0)
        leds[48-led+306] = (0,255,0)
        leds[48-led+307] = (255,0,255)
        leds[48-led+308] = (255,0,255)
        leds[48-led+309] = (255,0,255)
        client.put_pixels(leds)
        time.sleep(.1)

#SPOK#
def func10():
    for led in range(2,10):
        leds =[(0,0,0)]*360
        leds[48-led+64] = (255,218,185)
        leds[48-led+65] = (255,218,185)
        leds[48-led+66] = (255,218,185)
        leds[48-led+68] = (255,218,185)
        leds[48-led+69] = (255,218,185)
        leds[48-led+70] = (255,218,185)
        leds[48-led+4] = (255,218,185)
        leds[48-led+5] = (255,218,185)
        leds[48-led+9] = (255,218,185)
        leds[48-led+10] = (255,218,185)
        leds[48-led+121] = (255,218,185)
        leds[48-led+122] = (255,218,185)
        leds[48-led+124] = (255,218,185)
        leds[48-led+125] = (255,218,185)
        leds[48-led+126] = (255,218,185)
        leds[48-led+127] = (255,218,185)
        leds[48-led+128] = (255,218,185)       
        leds[48-led+129] = (255,218,185)
        leds[48-led+130] = (255,218,185)
        leds[48-led+182] = (255,218,185) 
        leds[48-led+183] = (255,218,185)
        leds[48-led+184] = (255,218,185)  
        leds[48-led+185] = (255,218,185)
        leds[48-led+186] = (255,218,185)
        leds[48-led+187] = (255,218,185)
        leds[48-led+188] = (255,218,185)
        leds[48-led+189] = (255,218,185)
        leds[48-led+190] = (255,218,185)        
        leds[48-led+243] = (255,218,185)
        leds[48-led+244] = (255,218,185)
        leds[48-led+245] = (255,218,185)
        leds[48-led+246] = (255,218,185)
        leds[48-led+247] = (255,218,185)
        leds[48-led+248] = (255,218,185)
        leds[48-led+249] = (255,218,185)
        leds[48-led+250] = (255,218,185)
        leds[48-led+305] = (255,218,185)
        leds[48-led+306] = (255,218,185)
        leds[48-led+307] = (255,218,185)
        leds[48-led+308] = (255,218,185)
        client.put_pixels(leds)
        time.sleep(.1)



        
while True:
    if value.isdigit() == True: #.isgigit()
        value = int(value)
        if value > 5 or value <1: #if value is outside our range:
            value = input("That option is not possible, try a number between 1 and 5")
            continue #skip rest of loop, start from isdigit() check again.
        else:
            break
    else:
        value = input("Don't try with letters, select a number:") # ask for new value



led = 0
while led<30: # si cambio a led<60 al cruzarse se cambian los colores
    for rows in range(6):
        leds[led + rows*60] = (255,255,0)
        leds[59-led + rows*60] = (255,0,255)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1
led = 0
while led<30:
    for rows in range(1,5):
        leds[29+led + rows*60] = (0,0,0)
        leds[30-led + rows*60] = (0,0,0)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1



if value == 1:
    func1()
    func0()
elif value == 2:
    func2()
elif value == 3:
    func3()
elif value == 4:
    func4()
elif value == 5:
    func5()
if panel_choice == 6:
    func6()
elif panel_choice == 7:
    func7()
elif panel_choice == 8:
    func8()
elif panel_choice == 9:
    func9()
elif panel_choice == 10:
    func10()


#STATEMENTS FOR RESULTS#
1 == 6 
1 > 3
6 > 3
1 == 6 
6 > 4
6 > 4
2 == 7 
7 > 1
7 > 1
2 == 7 
7 > 5
7 > 5
3 == 8 
8 > 4
8 > 4
3 == 8 
8 > 2
8 > 2
4 == 9 
9 > 2
9 > 2
4 == 9 
9 > 5
9 > 5
5 == 10 
10 > 3
10 > 3
5 == 10
10 > 1
10 > 1


if value < panel_choice:   
    print('LOSER')
    
elif value == panel_choice:
    print('RE-START')
    
else:
    print('WINNER')
