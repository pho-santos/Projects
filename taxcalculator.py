#tax calculator
#input - price, state
#output - subtotal, tax and total if WI
#input > transform to float > if(WI/else) > if total + tax > else total

def tot():
    while True:
        tot = input('Please, input the total of value of the purchase: ')
        if tot.replace('.','').isnumeric():
            tot = float(tot)
            return tot
        else:
            print('Please, input a number.')

print('Hello! I will help you calculate the amount of taxes you need to pay! Hope you\'re not from Wisconsin *wink*')
state = input('Please, input the State full name or abbreviation')
up_state = state.upper()
subtotal = tot()
tax = 0.055 * subtotal
total = subtotal + tax

if up_state == "WI" or up_state == "WISCONSIN":
    print(f'Your Subtotal = ${subtotal:.2f} \n Tax = ${tax:.2f} \n Total = ${total:.2f}')
else:
    print(f'There are no Taxes on this order, your total is ${subtotal:.2f}')
    




