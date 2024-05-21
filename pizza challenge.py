import math

def people(num):
    while True:
        try:
            pep = input('How many people are going to participate in the pizza party?')
            if pep.isnumeric() == True:
                return int(pep)
            else:
                print(f'Please, use intergers')
        except:
            print('Please, use intergers')

def slices(num):
    while True:
        try:
            piz = input('How many slices each??')
            if piz.isnumeric() == True:
                return int(piz)
            else:
                print(f'Please, use intergers')
        except:
            print('Please, use intergers')

people = people(0)
slices = slices(0)
pizzas = math.ceil(people * slices / 8)
print(f'{pizzas} pizzas will be needed')