import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

weapon_list = [1, 2, 3, 4, 5]

panel_choise = random.choice(weapon_list)

val = panel_choise

led=0
def func1(val):
    for led in range(360):
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
        return val**val;
def func2(val):
    for led in range(360):   
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
    return val**val;
def func3(val):
    for led in range(360): 
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
    return val**val;
def func4(val):
    for led in range(360):
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
    return val**val;
def func5(val):
    for led in range(360):
        leds =[(0,0,0)]*360
        leds[led+62] = (255,218,185)
        leds[led+63] = (81,81,81)
        leds[led+64] = (81,81,81)
        leds[led+65] = (81,81,81)
        leds[led+66] = (81,81,81)
        leds[led+67] = (81,81,81)
        leds[led+68] = (81,81,81)
        leds[led+69] = (81,81,81)
        leds[led+70] = (81,81,81)
        leds[led+71] = (255,218,185)
        
        leds[led+4] = (81,81,81)
        leds[led+5] = (81,81,81)
        leds[led+6] = (81,81,81)
        leds[led+7] = (81,81,81)
        leds[led+8] = (81,81,81)
        leds[led+9] = (81,81,81)
        
        leds[led+121] = (255,218,185)
        leds[led+122] = (255,218,185)
        leds[led+123] = (81,81,81)
        leds[led+124] = (255,218,185)
        leds[led+125] = (255,218,185)
        leds[led+126] = (255,218,185)
        leds[led+127] = (255,218,185)
        leds[led+128] = (255,218,185)       
        leds[led+129] = (255,218,185)
        leds[led+130] = (81,81,81)
        leds[led+131] = (255,218,185)
        leds[led+132] = (255,218,185)
        
        leds[led+181] = (255,218,185)      
        leds[led+182] = (255,218,185) 
        leds[led+183] = (81,81,81) 
        leds[led+184] = (255,218,185)  
        leds[led+185] = (255,218,185)
        leds[led+186] = (255,218,185)
        leds[led+187] = (255,218,185)
        leds[led+188] = (255,218,185)
        leds[led+189] = (255,218,185)
        leds[led+190] = (81,81,81)
        leds[led+191] = (255,218,185)
        leds[led+192] = (255,218,185)
        
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
    return val**val;


if val == 1:
    func1(val)
elif val == 2:
    func2(val)
elif val == 3:
    func3(val)
elif val == 4:
    func4(val)
elif val == 5:
    func5(val)
