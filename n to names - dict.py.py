#input = number of month
#output = month

def get_m(prompt):
    while True:
        try:
            month = int(input(prompt))
            if month in range(1,13):
                return month
            else:
                print('Please, input a number from 1 to 12')
        except:
            print('Please, input a number from 1 to 12')

def get_l(prompt):
    while True:
        try:
            lang = int(input(prompt))
            if lang in range(0,2):
                return lang
            else:
                print('Please, input 0 or 1')
        except:
            print('Please, input 0 or 1')

months = {
    1: ("JANUARY", "JANEIRO"),
    2: ("FEBRUARY", "FEVEREIRO"),
    3: ("MARCH", "MARÇO"),
    4: ("APRIL", "ABRIL"),
    5: ("MAY", "MAIO"),
    6: ("JUNE", "JUNHO"),
    7: ("JULY", "JULNHO"),
    8: ("AUGUST", "AGOSTO"),
    9: ("SEPTEMBER", "SETEMBRO"),
    10: ("OCTOBER", "OUTUBRO"),
    11: ("NOVEMBER", "NOVEMBRO"),
    12: ("DECEMBER", "DEZEMBRO")}

language = get_l('Please, input 0 for English or 1 for Portuguese. / Por favor, insira 0 para inglês ou 1 para Português.')
num = get_m('Please, input the number of the month, from 1 to 12: \n')
month = months[num][language]
print(f'Your month is {month}')


