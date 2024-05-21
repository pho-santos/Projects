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
        tm = input('Please, input the time: ')
        if tm.isnumeric():
            tm = int(tm)
            if tm > 0:
                return tm
        else:
            print(f'Please, insert a positive numeric value')

c = principal(0)
i = rate(0)
t = time(0)
amount = c*(1+i*t)
print(f'Your total amount computing the iterest is: ${amount:.2f}')