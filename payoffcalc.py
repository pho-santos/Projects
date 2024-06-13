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

def calc_m_until_paid(b, i, p):
    n = - (1 / 30) * math.log(1 + (b / p ) * ( 1 - (1 + i) ** 30)) / math.log(1 + i)
    n = math.ceil(n)
    print(f'It will take you {n} months to pay off this card debt.')

balance = get_value('Plese, inform your credit card balance: \n')
APR = (get_value('Please, inform your credit card\'s APR without the %: \n')/100)/365
m_pay = get_value('What is the monthly payment that you can make?: \n')
calc_m_until_paid(balance, APR, m_pay)