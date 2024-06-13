#input - word1, word2
#output - isanagram 
#input(check if is a word) -> check how many letters -> check if they are the same letters

def word_get(prompt):
    while True:
        w = input(prompt)
        if w.isalpha():
            return w
        else:
            print('Please, input a word.')

def is_anagram(w1, w2):
    if len(w1) == len(w2):
        w1_l = list(w1)
        w2_l = list(w2)
        wc_l = []
        for l in w1_l:
            if l in w2_l:
                wc_l.append(l)
            else:
                continue
        if len(wc_l) == len(w2_l):
            print(f'{w1} and {w2} are anagrams!')
        else:
            print(f'{w1} and {w2} are not anagrams.')
    else:
        print(f'Your words {w1} and {w2} have different lenghts, they can\'t be anagrams')

print(f'Hello! I\'m going to help you checking if two words are anagrams!')
word1 = word_get('Please, insert the first word: \n')
word2 = word_get('Please, insert the second word: \n')
is_anagram(word1, word2)
