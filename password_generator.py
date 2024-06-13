#inputs - min lenght, n special characterd, n of numbers
#output - password
import random
import clipboard

characters = {
            "numbers": ["1", "2", "3", "4", "5", "6", "7", "8", "9"], 
            "special": ["!", "@", "#", "$"], 
            "letters": list("abcefghi")
            }

def nums_get(prompt):
    print(prompt)
    while True:
        num = input()
        if num.isnumeric():
            return int(num)
        else:
            print('Please, input a integer.')

def password_gen(n_chars, n_spec_chars, n_num_chars):
    password = []
    for n in range(num_chars - num_numbers_chars - num_special_chars):
        password.append(random.choice(characters["letters"]))
    for n in range(0, num_numbers_chars):
        password.append(random.choice(characters["numbers"]))
    for n in range(0, num_special_chars):
        password.append(random.choice(characters["special"]))
    random.shuffle(password)
    return "".join(password)

def copy_pass(passwords):
    print("Which of the passwords do you want to copy to your clipboard? 1, 2 or 3?")
    while True:
        num = input()
        if num.isnumeric():
            if num in ["1", "2", "3"]:
                clipboard.copy(passwords[int(num) - 1])
                print(f'Password {num} successfully copied!')
                return
            else:
                print('Please, input 1, 2 or 3')
        else:
            print('Please, input a integer.')

num_chars = nums_get('Hello, how many characters your password is going to have?:')
num_special_chars = nums_get('How many of these characters are going to be special characters')
num_numbers_chars = nums_get('How many of these characters are going to be numeric characters')

if num_chars < num_numbers_chars + num_special_chars:
    print('The number of special characters + numeric charcters exced the totla password.')
else:
    password1 = password_gen(num_chars, num_special_chars, num_numbers_chars)
    password2 = password_gen(num_chars, num_special_chars, num_numbers_chars)
    password3 = password_gen(num_chars, num_special_chars, num_numbers_chars)

    print("Here are three different passwords with the specified parameters:")
    print(password1)
    print(password2)
    print(password3)

copy = copy_pass([password1, password2, password3])