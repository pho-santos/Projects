#input - time in milliseconds
#output - mean, minimum time, maximum time, std dev
import math
import pandas as pd

df = pd.read_csv("numbers.csv")
values = df['numbers'].values.tolist()

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

def std_dev(list):
    if len(list) == 0:
        return None
    sqrd_values = [(val - mean) ** 2 for val in list]
    mean_sqrd = mean_dataset(sqrd_values)
    stdev = math.sqrt(mean_sqrd)
    print(f'Your standard deviation is {stdev:.2f}')

print('Hello, we are going to help you calculate basic statistics from the data from your CSV.') 

if len(values) > 0:
    mean = mean_val(values)
    print(f'Your average is {mean}')
    print(f'Your maximum value is {max(values)}')
    print(f'Your minimum value is {min(values)}')
    std_dev(values)
else:
    print('No numbers were entered.')





         





