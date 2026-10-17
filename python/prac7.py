'''Write a Python function named 
find_longest_word that takes a sentence and 
returns the longest word in it. If there a tie, 
return the first longest word.'''

from itertools import count


def long_word(sen):
    words = sen.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

x = long_word('hi how you')
print(x)

