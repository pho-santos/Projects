#input: num with spaces
#output: list without spaces 
value_list = []
numbers = list(range(10))

def value_get(prompt):
    while True:
        value = input(prompt)
        if len(value) == 2:
            if " " in value:
                num_str = value.replace(" ", "")
                if num_str.isdigit():
                    value_list.append(int(num_str))
                        #value = value.strip() tira espaços
                else:
                    print('Please, insert a space in the value.')
            else:
                print('Please, insert a space in the value.')
        elif value.lower() == "done":
            print(f'Your inputed numbers are: {value_list}')
            break
        else:
            print('Please, only insert 2 characters, a number and a space.')

def filter_even_numbers(list):
    list_clean = [value for value in list if value % 2 == 0]
    print(f'Your even numbers inputed are {*list_clean,}')

print("I will help you get even numbers from inputed ones.")
value_get("Please input a number and a space bar input:\n")
filter_even_numbers(value_list)



