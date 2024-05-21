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

price1 = price(0)
quant1 = quant(0)
price2 = price(0)
quant2 = quant(0)
price3 = price(0)
quant3 = quant(0)
subtotal = (price1 * quant1) + (price2 * quant2) + (price3 * quant3)
tax = subtotal * 0.055
total = subtotal + tax

print(f'Item 1: {price1} * {quant1} ... {price1 * quant1} \n Item 2: {price2} * {quant2} ... {price2 * quant2} \n Item 3: {price3} * {quant3} ... {price3 * quant3} \n Subtotal ......... {subtotal} \n Tax ......... {tax} \n Total ......... {total}')

