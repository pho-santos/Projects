#first name, last name, id (aa-1234), zip code
#constrictions - fist and last name filled, having at least 2 characters, zip code is a number

def get_name(prompt):
    while True:
        name = input(prompt)
        if name.isalpha():
            if name == "":
                print(f'Your name can\' be blank.')
            elif len(name) < 2:
                print(f'Your name has to be at least two letters long.')
            else:
                name.capitalize()
                return name
        else:
            print(f'Please, only use letters.')
            
def get_idl(prompt):
    while True:
        letters = input(prompt)
        if letters.isalpha():
            if len(letters) == 2:
                letters = letters.upper()
                return letters
            else:
                print(f'Please, only insert two letters.')
        else:
            print(f'Please, only use letters.')

def get_idn(prompt):
    while True:
        nums = input(prompt)
        if nums.isnumeric():
            if len(nums) == 4:
                return nums
            else:
                print(f'Please, insert 4 numbers.')
        else:
            print(f'Please, insert only numbers.')

def get_zip(prompt):
    while True:
        nums = input(prompt)
        if nums.isnumeric():
            if len(nums) == 5:
                return nums
            else:
                print('Please, insert 5 numbers.')
        else:
            print(f'Please, input only numbers.')

def validate_input(prompt):
    print(prompt)
    f_name = get_name('Please, insert your name. Use only letters and at least 2 ones: \n')
    l_name = get_name('Please, insert your last name. Use only letters and at least 2 ones: \n')
    l = get_idl('Please, insert the two first letters of your ID. Only use letters: \n')
    n = get_idn('Please, insert the 4 numbers of your ID. Use only numbers: \n')
    id_c = l + "-" + n
    zip = get_zip('Please, insert your zip code. Insert only numbers: \n')
    print(f'Name: {f_name} {l_name} \nID: {id_c} \nZIP code: {zip} \nNo errors were found.')

validate_input('Hello, I\'m your information validator!')