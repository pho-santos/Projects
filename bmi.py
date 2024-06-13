#BMI calculator
#inputs - height, weight, system
#outpu - BMI, were in the range the person stands

def is_float(string):
    if string.replace('.','').isnumeric():
        return True
    else:
        return False

def get_system(prompt):
    while True:
        system = input(prompt).upper()
        if system == "M" or system == "I":
            return system
        else:
            print('Please, input M or I.')

def get_hw(prompt1, prompt2):
    while True:
        h = input(prompt1)
        if is_float(h):
            h = float(h)
            w = input(prompt2)
            if is_float(w):
                w = float(w)
                return h, w
            else:
                print('Please, insert a positive number for you weight.')
        else:
            print('Please, insert a positive number for your height.')

def calc_bmi(h, w, sys):
    if sys == "I":
        h = h*12
        bmi = (w/(h*h))*703
    else:
        bmi = w/(h*h)
    if 18.5 <= bmi <= 25.0:
        print(f'Your BMI is {bmi}, it is within the ideal weight range')
    elif bmi < 18.5:
        print(f'Your BMI is {bmi}, it is lower than the ideal weight range')
    else:
        print(f'Your BMI is {bmi}, it is over the ideal weight range')

sys = get_system('Please, input the desired system, M for Metric or I for Imperial: \n')
h, w = get_hw('Please, insert your Height: \n', 'Please, insert your Weight: \n')
result = calc_bmi(h, w, sys)