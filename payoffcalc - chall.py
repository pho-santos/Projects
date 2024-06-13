#Months to pay credit card debt calculator
#inputs: balance, APR, monthly payment
import math

def is_float(string):
    if string.replace('.','').isnumeric():
        return True
    else:
        return False

def get_value(prompt):
    while True:
        value = input(prompt)
        if is_float(value):
            value = float(value)
            return value
        else:
            print(f'Please, input a positive numeric value')

def how_much_to_pay(b, i, n):
    n = - (1 / 30) * math.log(1 + (b / p ) * ( 1 - (1 + i) ** 30)) / math.log(1 + i)
    n = math.ceil(n)
    print(f'It will take you {n} months to pay off this card debt.')

def calc_m_until_pai(b, i, n):

balance = get_value('Plese, inform your credit card balance: \n')
APR = (get_value('Please, inform your credit card\'s APR without the %: \n')/100)/365
#m_pay = get_value('What is the monthly payment that you can make?: \n')
months = get_value('In how many months do you want to pay your debt? : \n')
how_much_to_pay(balance, APR, months)