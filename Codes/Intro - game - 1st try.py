value = input('''Welcome to LEDs Invaders
              \t 1. Easy
              \t 2. Normal
              \t 3. Difficult
              Type the number of yout choise and press enter.''') # \n-newline; \t- tab

def func1(val):
    return val**val;
def func2(val):
    return val**val;
def func3(val):
    return val**val;

while True:
    if value.isdigit() == True: #.isgigit()
        value = int(value)
        if value > 3 or value < 1: #if value is outside our range:
            value = input("That option is not possible, try a number between 1 and 3")
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
    

