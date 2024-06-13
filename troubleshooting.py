menu = 0

print('Hello! I will help you troubleshoot the problems with your car!')

while menu == 0:
    q1 = input("Is the car silent when you turn the key? Answer y/n \n")
    if q1 == "y":
        q2_1 = input("Are the battery terminals corroded? Answer y/n \n")
        if q2_1 == "y":
            print('Clean terminals and try starting again.')
            menu = 1
        elif q2_1 == "n":
            print("Replace cables and try again.")
            menu = 1
        else:
            print("Please, insert y/n")
    elif q1 == "n":
        q2_2 = input("Does the car make a clicking noise? Answer Y/N \n").upper
        if q2_2 == "Y":
            print(f'Replace the battery.')
            menu = 1
        elif q2_2 == "N":
            q3 = input("Does the car crank up but fail to start? Answer Y/N \n").upper
            if q3 == "Y":
                print(f'Check spark plug connections')
                menu = 1
            elif q3 == "N":
                print(f"Does the engine start and then die?")
                q4 = input("Does your car have fuel injection? Answer Y/N \n").upper
                if q4 == "Y":
                    print(f'Get it in for service.')
                    menu = 1
                elif q4 == "N":
                    print(f'Check to ensure the choke is opening and closing.')
                    menu = 1
                else:
                    print("Please, insert y/n")
    else:
        print("Please, insert y/n")
        
