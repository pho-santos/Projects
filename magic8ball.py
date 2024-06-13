#input - question
#process list answers, random module to chose which answer
#output - yes, no, maybe, ask again

import random
answers = ['Yes', 'No', 'Maybe', 'Ask Again']

question = input('Hello! What\'s your question?:\n')
print(f'{answers[random.randint(0,3)]}')
#print(f'{answers[random.choice(answers)]}')

