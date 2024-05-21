#temperature 
#input - conversion. temperature

def is_float(string):
    if string.replace('.','').isnumeric():
        return True
    else:
        return False

def get_temperature(prompt):
    while True:
        temperature = input(prompt)
        if is_float(temperature):
            temperature = float(temperature)
            return temperature
        else:
            print('Please, input a numeric value')

def get_conversion(prompt):
    while True:
        conversion = input(prompt).upper()
        if conversion == "C" or conversion == "F" or conversion == "K":
            return conversion
        else:
            print('Please, C, F or K')

def calculate(original, conversion):
    if original == "C":
        if conversion == "F":
            temperature_c = (temperature_o * 9 / 5) + 32
            print(f'Original = {temperature_o}C, Converted = {temperature_c}F')
        if conversion == "K":
            temperature_c = temperature_o + 273.15
            print(f'Original = {temperature_o}C, Converted = {temperature_c}K')
        else:
            print(f'Can\'t convert C to C, Duh!')
    elif original == "F":
        if conversion == "C":
            temperature_c = (temperature_o - 32) * 5 / 9
            print(f'Original = {temperature_o}F, Converted = {temperature_c}C')
        if conversion == "K":
            temperature_c = (temperature_o - 32) * (5/9) + 273.15
            print(f'Original = {temperature_o}F, Converted = {temperature_c}K')
        else:
            print(f'Can\'t convert F to F, Duh!')
    elif original == "K":
        if conversion == "C":
            temperature_c = temperature_o - 273.15
            print(f'Original = {temperature_o}K, Converted = {temperature_c}C')
        if conversion == "F":
            temperature_c = (temperature_o - 273.15) * (9/5) + 32
            print(f'Original = {temperature_o}K, Converted = {temperature_c}F')
        else:
            print(f'Can\'t convert K to K, Duh!')
    else:
        print('Program Error, please, run it again and follow the input instructions.')

temperature_o = get_temperature('Please, input the temperature: \n')
original = get_conversion('Please, input C for Celsius, F for Fahrenheit or K for Kelvin: \n')
conversion = get_conversion('What will it be converted to? input C for Celsius, F for Fahrenheit or K for Kelvin: \n')
result = calculate(original, conversion)

