#input - time in milliseconds
#output - mean, minimum time, maximum time, std dev
import math
values = []

def nums_get():
    while True:
        num = input()
        if num.isnumeric():
            values.append(int(num))
            return
        elif num == "done" or num == "Done":
            values.append(num.upper())
            return
        else:
            print('Please, input a integer or "Done" if you want to finish the inputing process.')

def mean_val(list):
    if len(list) == 0:
        return 0
    total = 0
    for val in list:
        total += val
    mean = total / len(list)
    return mean

def mean_dataset(list):
    if len(list) == 0:
        return 0
    total = 0
    for val in list:
        total += val
    mean = total / (len(list) - 1)
    return mean

def max_val(list):
    if len(list) == 0:
        return None
    max = 0
    for val in list:
        if max < val:
            max = val
        else:
            continue
    print(f'Your maximum value is {max}')

def min_val(list):
    if len(list) == 0:
        return None
    min = 9999999999999999999999
    for val in list:
        if min > val:
            min = val
        else:
            continue
    print(f'Your minimum value is {min}')

def std_dev(list):
    if len(list) == 0:
        return None
    sqrd_values = [(val - mean) ** 2 for val in list]
    mean_sqrd = mean_dataset(sqrd_values)
    stdev = math.sqrt(mean_sqrd)
    print(f'Your standard deviation is {stdev:.2f}')

print('Hello, we are going to help you calculate basic statistics from inputed data.')
print('Please, input the numbers and when you want to get your statistics, insert the word "Done".')

while "DONE" not in values:
    nums_get()

values.remove("DONE")

if len(values) > 0:
    mean = mean_val(values)
    print(f'Your average is {mean}')
    max_val(values)
    min_val(values)
    std_dev(values)
else:
    print('No numbers were entered.')





         





