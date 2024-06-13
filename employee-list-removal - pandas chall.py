#https://www.geeksforgeeks.org/python-read-csv-columns-into-list/ - reading csv with csv or pandas
#https://encurtador.com.br/WUBVB - removing lines with pandas
import pandas as pd

df = pd.read_csv('employees_date.csv')
names = df['Name'].tolist() # converting column data to list

def removal(prompt):
    while True:
        to_remove = input(prompt)
        if to_remove in names:
            return to_remove
        else:
            print('Please input one of the names mentioned before.')

print(f'There are {len(names)} employees:')
for name in names:
    print(f'{name}')

remove = removal('Please, insert which employee do you want to remove (use the exact ):\n')

df = df.drop(df[df.Name == remove].index)
df.to_csv('employees_data.csv', index=False)