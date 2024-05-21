#pizza
#input: people, pizzas
#outputs: pizzas/people, leftovers
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

def pizza(num):
    while True:
        try:
            piz = input('How many pizzas were ordered?')
            if piz.isnumeric() == True:
                return int(piz) * 8
            else:
                print(f'Please, use intergers')
        except:
            print('Please, use intergers')

print(f'Hello, i\'m the pizza helper!')

people = people(0)
pizza = pizza(0)
result = math.floor(pizza / people)
left = pizza % people

if result == 1 and left == 1:
    print(f'Each one will have {result} slice of pizza and there will be {left} leftover piece')
elif result == 1:
    print(f'Each one will have {result} slice of pizza and there will be {left} leftover pieces')
elif result >= 2 and left == 1:
    print(f'Each one will have {result} slices of pizza and there will be {left} leftover piece')
else:
    print(f'Each one will have {result} slices of pizza and there will be {left} leftover pieces')





