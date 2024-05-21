def get_age(prompt):
    while True:
        age = input(prompt)
        if age.isnumeric():
            age = int(age)
            return age
        else:
            print('Please, input a valide interger')

countries = {
    "USA": 16,
    "BRA": 18,
    "NIG": 23,
    "IND": 18,
    "FRA": 17,
    "UK": 17
}

keys = countries.keys()
print("Countries available:", list(keys))
place = input('Please, input one of the countries above \n').upper()
legal_age = countries.get(place)
your_age = get_age('Please, input your age: \n')

can_drive = "you can legally drive" if legal_age <= your_age else "you can't legally drive"
print(can_drive)