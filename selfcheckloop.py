#ex 10 - check out
#input - prices, quantity
#output - subtotal, taxes

def is_float(inp):
    if inp.replace(".","").isnumeric():
        return True
    else:
        return False

def price(pri):
    while True:
        pri = input("Insert the price of the item: ")
        if is_float(pri):
            pri = float(pri)
            if pri > 0:
                return pri
            else:
                print("Insert a positive valid value")                
        else:
            print("Insert a positive valid value")

def quant(qt):
    while True:
        qt = input("Insert the quantity of the item: ")
        if qt.isnumeric:
            qt = int(qt)
            if qt > 0:
                return qt
            else:
                print("Insert a positive valid value")                
        else:
            print("Insert a positive valid value")   

num_items = int(input("How many items do you want to check out?"))
prices = []

for i in range(num_items):
    print(f'Item {i+1}')
    pri = float(price(0))
    qt = float(quant(0))
    pri_qt = pri * qt
    prices.append(pri_qt)

subtotal = sum(prices)
tax = subtotal * 0.055
total = subtotal + tax    

for i, price in enumerate(prices, start=1):
    print(f'Price of item {i}: ${price: .2f}')
print(f'Sub total: {subtotal: .2f}')
print(f'Taxes: ${tax: .2f}')
print(f'Total: ${total: .2f}')

