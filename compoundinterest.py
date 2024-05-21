#ex12 simple interest
#inputs - principal, rate, time
#outpu - amount

def is_float(fra):
    while True:
        if fra.replace('.','').isnumeric():
            return True
        else:
            return False

def principal(fra):
    while True:
        prin = input('Please, input the principal: ')
        if is_float(prin):
            prin = float(prin)
            if prin > 0:
                return prin
        else:
            print(f'Please, insert a positive numeric value')
    
def rate(fra):
    while True:
        rt = input('Please, input the interest rate: ')
        if is_float(rt):
            rt = float(rt)
            if rt > 0:
                rt = rt/100
                return rt
        else:
            print(f'Please, insert a positive numeric value')

def time(fra):
    while True:
        tm = input('Please, input the amount of years: ')
        if tm.isnumeric():
            tm = int(tm)
            if tm > 0:
                return tm
        else:
            print(f'Please, insert a positive numeric value')

def compound(fra):
    while True:
        times = input('Please, input how many times the interest is compounded in the year: ')
        if times.isnumeric():
            times = int(times)
            if times > 0:
                return times
        else:
            print(f'Please, insert a positive numeric value')

c = principal(0)
i = rate(0)
t = time(0)
n = compound(0)
amount = c*(1+(i/t))**t*n
print(f'Your total amount, using a principal {c}, computing the iterest {i}, compunded {n} times in {t} years is: ${amount:.2f}')