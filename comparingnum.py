#input - n amount of numbers
#output - bigger
def qt_get(prompt):
    while True:
        qt = input(prompt)
        if qt.isnumeric:
            qt = int(qt)
            return qt
        else:
            print('Please, input an interger.')

def ns_get(prompt, qt):
    nums = []
    iterations = 0
    print(prompt)
    while iterations < qt:
        num = input(f'Please, input the number {iterations + 1}: \n')
        if num.isnumeric():
            num = int(num)
            if num in nums:
                print(f'Please, input a number that wasn\'t already inputed.\nNumbers already inputed: {nums}')
            else:
                nums.append(num)
                iterations += 1
        else:
            print(f"Please, input an interger")
    print(f'Numbers inputed: {nums}')
    return nums

def bigger(nums):
    biggest = 0
    for num in nums:
        if num > biggest:
            biggest = num
    print(f'The biggest number that was inputed is {biggest}, careful, he is really big.')
#exercício pediu para criar um algoritimo, mas a função max(list) acha mais fácil exemple a baixo:
#def bigger(nums):
#    biggest = max(nums)  # Using the max function to find the biggest number
#    print(f'The biggest number that was inputted is {biggest}, careful, he is really big.')

qt = qt_get(f'Hello! How many number would you like to input to check which is the biggest?: \n') 
nums = ns_get(f"Time to input {qt} numbers to be checked", qt)
bigger(nums)