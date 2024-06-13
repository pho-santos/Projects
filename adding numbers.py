#input - 5 numbers
#output - addition

def is_float(n):
    n = n.replace(".","")
    if n.replace("-","").isnumeric():
        return True
    else:
        return False
    
def qt_get(prompt):
    while True:
        qt = input(prompt)
        if qt.isnumeric():
            return int(qt)
        else:
            print(f'Please, input only interger values.')

def num_get(q):
    total = 0.0
    n_list = []
    print(f'Please, you\' goingo to have to inser {q} numbers.')
    for n in range(1,q + 1):
        num = input(f'Please, insert your {n} number:\n')
        if is_float(num):
            num = float(num)
            n_list.append(num)
            total += num
        else:
            n_list.append(num)
    return n_list, total

q = qt_get(f'Please, input the quantity of numbers you want to add:\n')
n_list, total = num_get(q)
print(f'Your numbers inputed are {n_list}.\nYour total is = {total}.')

        


