#area of a room
#inputs - width and lenght
#outputs - area in feet and meters

def is_float(ipt):
    if ipt.replace('.','').isnumeric():
        return True
    else:
        return False

def wdtm(num):
    while True:
        try:
            width = input('Please, input the width of the room in meters:')
            if is_float(width) == True:
                width = float(width)
                if width > 0:
                    return width
        except:
            print(f'Please, insert a numerical value')

def lgtm(num):
    while True:
        try:
            lenght = input('Please, input the lenght of the room in meters:')
            if is_float(lenght) == True:
                lenght = float(lenght)
                if lenght > 0:
                    return lenght
        except:
            print(f'Please, insert a numerical value')

def wdtf(num):
    while True:
        try:
            width = input('Please, input the width of the room in feet:')
            if is_float(width) == True:
                width = float(width)
                if width > 0:
                    return width
        except:
            print(f'Please, insert a numerical value')

def lgtf(num):
    while True:
        try:
            lenght = input('Please, input the lenght of the room in feet:')
            if is_float(lenght) == True:
                lenght = float(lenght)
                if lenght > 0:
                    return lenght
        except:
            print(f'Please, insert a numerical value')

f_m = input('Would you like to use feet or meters to calculate the area?')

if f_m == "meters":
    width = wdtm(0)
    lenght = lgtm(0)
    aream = width * lenght
    areaf = aream*3.28084
    print(f'Using the dimensions {width}m x {lenght}m, you have a {aream} square meter or {areaf} square feet room.')
elif f_m == "feet":
    width = wdtf(0)
    lenght = lgtf(0)
    areaf = width * lenght
    aream = areaf*0.09290304
    print(f'Using the dimensions {width}f x {lenght}f, you have a {areaf} square feet or {aream} square meters room.')
else:
    print('Please, input the word feet or meters.')

