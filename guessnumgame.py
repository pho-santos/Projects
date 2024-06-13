#inputs - difficulty, number
#process - generate number
#outputs - if correct, hints, number of guesses
import random

def get_lv(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num in range(1, 4):
                return num
            else:
                print('Please, input 1, 2 or 3.')
        except:
            print('Please, input 1, 2 or 3.')

def num_game(prompt):
    print(prompt)
    lv = get_lv('Which level are you going to try? 1 (1 to 10), 2 (1 to 100) or 3 (1 to 1000):\n')

    if lv == 1:
        max_num = 10
    elif lv == 2:
        max_num = 100
    else:
        max_num = 1000

    num = random.randint(1, max_num)
    num_guesses = 0
    guess_list = []
    print(f'Great, let level {lv} begin!')
    print('Remember, only input positive numbers. Everything else is going to be counted as a missed guess.')

    while True:
        #print(num) #for testing
        guess = input('Your guess is: \n')
        if guess.isnumeric():
            guess = int(guess)
            if guess == num:
                num_guesses += 1
                print(f'Congratulations! You guessed the number in {num_guesses} guesses')
                return
            else:
                num_guesses += 1
                guess_list.append(guess)
                if guess < num:
                    print(f'Your guess, {guess}, was smaller than the number')
                elif guess > num:
                    print(f'Your guess, {guess}, was bigger than the number')
                print(f'The numbers you already inputed are {guess_list}.')
        else:
            num_guesses += 1
            print('Please, input only positive integers.')

num_game('Welcome, to Guess the Numberrrr! I\' your host, Number Bot 500.')