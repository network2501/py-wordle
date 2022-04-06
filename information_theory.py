#
#   Space of probabilities
#
#   p(□□□□□) = (words excluded)/12972 = ??
#   I(□□□□□) log₂(1/p) = ???
#
#   E[Information] = (Σ/x)p(x)·(something)
#
#   Correct letter is in the word and in the correct spot.  (green/orange)
#   Present letter is in the word but in the wrong spot.    (yellow/blue)
#   Absent letter is not in the word in any spot.           (grey)

from logging import error
from allowed_words import words
#from requests import request
from math import log2
import time
startTime = time.time()

const_possbility_space = int(12961)


first_guess = 'salet'

wordls = words

used = []
duplicate_worlds = words
left_over = []



# seems more resilient, for words with more than 1 letter matched
# Counter({'s': 8918, 'l': 7468, 'a': 5655, 't': 4642, 'e': 3159})
# 865 goal
# 3159 returned


# def wordpass():
#     for letter in 'slate':
#         for word in wordls:
#             if letter in word:
#                 duplicate_worlds.remove(word) 
#             used.append(letter)

# Counter({'s': 6714, 'l': 6079, 't': 5600, 'a': 5161, 'e': 4476})
# 865 goal
# 6714 returned


# def wordpass():
#    for word in wordls:
#        for letter in 'slate':
#            try:
#                if letter in word:
#                    duplicate_worlds.remove(word) 
#            except ValueError:
#                continue
#            used.append(letter)





def wordpass():
    words_to_remove = set()
    # do this for each of the 12k words 
    for word in wordls:
        # for nth letter in the word guess 
        # check if the word has already been
        # added to the words to remove
        # otherwise  
        for letter in first_guess:
            if word not in words_to_remove:
                if letter in word:
                    words_to_remove.add(word)
                else:
                    pass
            else:
                pass
    #print(words_to_remove)
    for i in words_to_remove:
        duplicate_worlds.remove(i)
    return duplicate_worlds


#print(wordpass())
p1 = len(wordpass())
print(f"\nFrom 12972 we're left with {p1}")
value1 = round(p1/const_possbility_space,4)
print(f'p(□□□□□) = {p1}/12972 = {value1}')
i = round(log2(1/value1),2)
print(f'I(□□□□□) log₂(1/{value1}) = {i}')


executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))



#print(Counter(used))
#print(f"865 goal\n{len(duplicate_worlds)} returned")   
