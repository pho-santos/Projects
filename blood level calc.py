#ex 17 - blood alcohol calc
#inputs - weight, gender, number of drinks, alcohol%, time of last drink 

def is_float(string):
    if string.replace(".","").isnumeric():
        return True
    else:
        return False

def get_gender(prompt):
    while True:
        gender = input(prompt).upper()
        if gender == "FEMALE" or gender == "MALE":
            return gender
        else:
            print('Please, input FEMALE or MALE')

def get_system(prompt):
    while True:
        system = input(prompt).upper()
        if system == "METRIC" or system == "IMPERIAL":
            return system
        else:
            print('Please, put metric or imperial')
            
def get_country(prompt):
    while True:
        country = input(prompt).upper()
        if country == "USA" or country == "ENGLAND" or country == "SCOTLAND":
            return country
        else:
            print('Please, input USA, ENGLAND or SCOTLAND')

def get_weight(prompt):
    while True:
        weight = input(prompt)
        if is_float(weight) == True:
            weight = float(weight)
            if weight > 0:
                return weight
            else:
                print('Please, input a positive number: \n')            
        else:
            print('Please, input a positive number: \n')

def get_drinks(prompt):
    while True:
        drinks = input(prompt)
        if drinks.isnumeric() == True:
            drinks = int(drinks)
            if drinks > 0:
                return drinks
            else:
                print('Please, input a positive number: \n')            
        else:
            print('Please, input a positive number: \n')

def get_alcohol(prompt):
    while True:
        alcohol = input(prompt)
        if is_float(alcohol) == True:
            alcohol = float(alcohol)
            alcohol = alcohol
            if alcohol > 0:
                return alcohol
            else:
                print('Please, input a positive number: \n')            
        else:
            print('Please, input a positive number: \n')

def get_time(prompt):
    while True:
        time = input(prompt)
        if time.isnumeric() == True:
            time = int(time)
            if time > 0:
                return time
            else:
                print('Please, input a positive number: \n')            
        else:
            print('Please, input a positive number: \n')

gender = get_gender('Please, input your gender, female or male: \n')
system = get_system('Please, input which system you want to use: \n')
weight = get_weight('Please, input your weight: \n')
n_drinks = get_drinks('Please, input the number of drinks: \n')
alcohol = get_alcohol('Please, input the quantity of alcohol ingested per drink \n')
time = get_time('Please, input the last time you drank in hours: \n')
country = get_country('Please, Input USA, ENGLAND or SCOTLAND.\n')

if system == "IMPERIAL":
    if gender == "FEMALE":
        BAC = (n_drinks*alcohol*5.14/weight*0.66)-.015*time
        if country == "USA" or country == "ENGLAND":
            print(f'Your Blood Alcohol level is {BAC}')
            can_drive = "You can legally drive" if BAC < 0.08 else "you can\'t legally drive"
            print(can_drive)
        else:
            print(f'Your Blood Alcohol level is {BAC}')
            can_drive = "You can legally drive" if BAC < 0.05 else "you can\'t legally drive"
            print(can_drive)
    elif gender == "MALE":
        BAC = (n_drinks*alcohol*5.14/weight*0.73)-.015*time
        if country == "USA" or "ENGLAND":
            print(f'Your Blood Alcohol level is {BAC}')
            can_drive = "You can legally drive" if BAC < 0.08 else "you can\'t legally drive"
            print(can_drive)
        else:
            print(f'Your Blood Alcohol level is {BAC}')
            can_drive = "You can legally drive" if BAC < 0.05 else "you can\'t legally drive"
            print(can_drive)
    else:
        print('Please, correct the gender.')
elif system == "METRIC":
    if gender == "FEMALE":
        BAC = (n_drinks*alcohol*5.14/weight*0.66)-.015*time
        if country == "USA" or "ENGLAND":
            print(f'Your Blood Alcohol level is {BAC}')
            can_drive = "You can legally drive" if BAC < 0.08 else "you can\'t legally drive"
            print(can_drive)
        else:
            print(f'Your Blood Alcohol level is {BAC}')
            can_drive = "You can legally drive" if BAC < 0.05 else "you can\'t legally drive"
            print(can_drive)
    elif gender == "MALE":
        BAC = (n_drinks*alcohol*5.14/weight*0.73)-.015*time
        if country == "USA" or "ENGLAND":
           print(f'Your Blood Alcohol level is {BAC}')
           can_drive = "You can legally drive" if BAC < 0.08 else "you can\'t legally drive"
           print(can_drive)
        else:
           print(f'Your Blood Alcohol level is {BAC}')
           can_drive = "You can legally drive" if BAC < 0.05 else "you can\'t legally drive"
           print(can_drive)
    else:
        print('Please, correct the gender.')


