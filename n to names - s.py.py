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

month = get_m('Please, input the number of the month, from 1 to 12: \n')

match month:
    case 1:
        print('January')
    case 2:
        print('February')
    case 3:
        print('March')
    case 4:
        print('April')
    case 5:
        print('May')
    case 6:
        print('June')
    case 7:
        print('July')
    case 8:
        print('August')
    case 9:
        print('September')
    case 10:
        print('Octorber')
    case 11:
        print('November')
    case 12:
        print('December')
