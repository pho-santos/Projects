#input - names
#output - winner

import random

names = []

def get_name(prompt):
    while True:
        name = input(prompt)
        if len(name) == 0:
            print('Please, insert a name.')
        else:
            return name

def get_num(prompt):
    while True:
        num = input(prompt)
        if num.isnumeric():
            return int(num)
        else:
            print('Plese, input a positive integer.')

def winner_random_picker():
    global quant
    participants = 0
    while participants < quant:
        name_add = get_name('Please, insert a participant\'s name:\n')
        names.append(name_add)
        participants += 1
    draw_winner()
    

def draw_winner():
    global quant
    print('Great, the winner is going to be drew from the following names:')
    for name in names:
        print(f'{name}')
    winner = names[random.randint(0, quant-1)]
    print(f'Your winner is {winner}, congratulations!')
    names.remove(winner)
    quant -= 1

print('Let\'s help you pick a random winner!')

quant = get_num('How many participants are going to enter loterry?\n')

winner_random_picker()

keep_going = get_num(f'If you want to choose another winner, input 1, else input any number to close the program:\n')
while keep_going == 1 and quant > 0:
    draw_winner()
    if quant > 0:
        keep_going = get_num(f'If you want to choose another winner, input 1, else input any number to close the program:\n')
    else:
        print('There are no more participants.')

