#ex11
#input - money, exchange rate
#output - converted amount
import datetime

def is_float(f):
    if f.replace('.','').isnumeric():
        return True
    else:
        return False

def money(qt):
    while True:
        qt = input(f'Please, insert how many Euros do you want to convert to Dollars')
        if is_float(qt):
            qt = float(qt)
            if qt > 0:
                return qt
            else:
                print('Please, input a positive value')
        else:
            print('Please, imput a numeric value')

rate_dtu = 1.08763
rate_etd = 0.919433    
euro = money(0)
doll = euro * rate_etd
today = datetime.date.today()

print(f'€{euro} are U${doll:.2f} in {today}\'s conversion rate')