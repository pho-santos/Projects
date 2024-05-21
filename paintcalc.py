#paint calc
#input - length and width
#output - how many gallons

import math

print('Let\'s calculate how many gallons of paint you need!')

def is_float(phrase):
    if phrase.replace(".","").isnumeric():
        return True
    else:
        return False

def lenght(num):
    while True:
        leng = input('The lenght of the room in feet:')
        if is_float(leng) == True:
            return float(leng)
        else:
            print('Insert a number, please.')

def width(num):
    while True:
        wdt = input('The width of the room in feet:')
        if is_float(wdt) == True:
            return float(wdt)
        else:
            print('Insert a number, please.')

def radius(num):
    while True:
        rad = input('The radius of the room in feet:')
        if is_float(rad) == True:
            return float(rad)
        else:
            print('Insert a number, please.')

menu = 0
while menu == 0:
    shape = input(f'Which shape of room do you want to calculate, square, round or l-shaped?')
    if shape == "square":
        lenght = lenght(0)
        width = width(0)
        gallons = math.ceil(lenght * width / 350)
        print(f'You will need {gallons} gallons of paint.')
        menu = 1
    elif shape == "round":
        radius = float(radius(0)**2)
        gallons = math.ceil(radius * 3.14159 / 350)
        print(f'You will need {gallons} gallons of paint.')
        menu = 1
    elif shape == "l-shaped":
        print(f'To calculate the area of a l-shaped room, we will ask of you to separate it into two rectangles.')
        lenght1 = lenght(0)
        width1 = width(0)
        lenght2 = lenght(0)
        width2 = width(0)
        rec1 = lenght1*width1
        rec2 = lenght2*width2
        gallons = math.ceil((rec1 + rec2)/350)
        print(f'You will need {gallons} gallons of paint.')
        menu = 1
    else:
        print('Please, input one of the following words: square, round or l-shaped')






