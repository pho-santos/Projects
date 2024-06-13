#input = age, resting heart rate
#output - intensity 55% to 95% (table form) 

s

def rh_rate_calc(age, resthr):
    print('Intensity    | Rate')
    print('_____________|__________')
    for intensity in range(55, 100, 5):
        hrate = (((220 - age) - resthr) * (intensity / 100)) + resthr
        print(f'{intensity}%          | {hrate:.1f} bpm')

age = get_number('Please, insert your age. Input only positive integers. \n')
rh_rate = get_number('Please, insert your resting heart rate. Input only positive integers. \n')
rh_rate_calc(age, rh_rate)


