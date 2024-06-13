#https://www.geeksforgeeks.org/python-read-csv-columns-into-list/ - reading csv with csv or pandas
#https://encurtador.com.br/WUBVB - removing lines with pandas

import csv

names = []

filename = open('employees_date.csv', 'r')
file = csv.DictReader(filename)
for col in file:
    names.append(col['Name'].upper())

def removal(prompt):
    while True:
        to_remove = input(prompt).upper()
        if to_remove in names:
            return to_remove
        else:
            print('Please input one of the names mentioned before.')

print(f'There are {len(names)} employees:')
for name in names:
    print(f'{name}')

names.remove(removal('Please, insert which employee do you want to remove:\n'))

print(f'There are {len(names)} employees:')
for name in names:
    print(f'{name}')

