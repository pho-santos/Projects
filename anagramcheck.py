#input - word1, word2
#output - isanagram 
#input(check if is a word) -> check how many letters -> check if they are the same letters

def is_float(string):
    if string.replace('.','').isnumeric():
        return True
    else:
        return False

def word_get(prompt):
    while True:
        w = input(prompt)
        if is_float(w):
            print('Please, input a word.')
        else:
            return w

def is_anagram(w1, w2):
    if len(w1) == len(w2):
        if sorted(w1) == sorted(w2):
            print(f'{w1} and {w2} are anagrams!')
        else:
            print(f'{w1} and {w2} aren\'t anagrams!')
    else:
        print(f'Your words {w1} and {w2} have different lenghts, they can\'t be anagrams')

print(f'Hello! I\'m going to help you checking if two words are anagrams!')
word1 = word_get('Please, insert the first word: \n')
word2 = word_get('Please, insert the second word: \n')
is_anagram(word1, word2)
