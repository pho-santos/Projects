def is_float(fra):
    while True:
        if fra.replace('.','').isnumeric():
            return True
        else:
            return False

def get_purchase(prompt):
    while True:
        purchase = input(prompt)
        if is_float(purchase):
            purchase = float(purchase)
            if purchase > 0:
                return purchase
        else:
            print(f'Please, insert a positive numeric value')

def get_sct(prompt1, prompt2):
    while True:
        state = input(prompt1).upper()
        if state in state_list_ab or state in state_list_full:
            if state in ["WISCONSIN", "WI"]:
                county = input(prompt2).upper()
                if county in wisconsin_counties:
                    if county == "EAU CLAIRE":
                        tax = 0.005 if county == "EAU CLAIRE" else 0.004 if county == "DUNN" else 0
                        return state, county, tax
                else:
                    print(f'Please, input a county from Winsconsin {wisconsin_counties}')
            elif state in {"ILLINOIS", "IL"}:
                return state, {}, 0.08
            else:
                return state, {}, 0
        else:
            print(f'Please, input a state from the ones below: \n {state_list_ab}')


state_list_ab = ["AL", "AK", "AZ", "CO", "DE", "FL", "IL", "LA", "NY", "TX", "WA", "WI"]
state_list_full = ["ALABAMA", "ALASKA", "ARIZONA","COLORADO", "DELAWARE", "FLORIDA", "ILLINOIS", "LOUISIANA", "NEW YORK", "TEXAS", "WASHINGTON", "WISCONSIN" ]
wisconsin_counties = ["ASHLAND", "ADAMS","BAYFIELD", "CLARK", "DUNN", "EAU CLAIRE", "FOREST"]

print(f'Hello! I will help you calculate any taxes that fall upon your purchase')
print(f'Keep in mind the following state to correctly input your data: \n {state_list_full} \n the USPS abbreviations below can be used too \n {state_list_ab}')
state, county, tax = get_sct("Which state are you from?\n", "Which county in Wisconsin are you from?\n")
subtotal = get_purchase("Input the total value of your purchase: \n")
p_tax = subtotal * tax
total = subtotal + p_tax

if state == "WINCONSIN" or state == "WI" or state == "ILLINOIS" or state == "IL":
    print(f'Subtotal = ${subtotal:.2f} \n Tax = ${p_tax:.2f} \n Total = ${total:.2f}')
else:
    print(f'Total = ${total:.2f}')

