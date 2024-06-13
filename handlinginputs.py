#input - rate of return
#output

def is_float(n):
    if n.replace('.', '').isnumeric():
        return True
    else:
        return False

def r_get(prompt):
    while True:
        n = input(prompt)
        if n == '0':
            print('You can\'t divide by zero.')
        elif is_float(n):
            return float(n)
        else:
            print('Please, input a positive number.')

r = r_get(f'Hello, i will help you estimate how long will it take for you to double your investment. Please insert you rate of return:\n')
years = 72 / r
print(f'It will take {years} years to double your investment.')






