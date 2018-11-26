"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
SPECIAL = "!@$^&()"

word_string = input("Enter string that consists of #, %, *")
print(word_string)


def is_valid_format(word_format):
    for char in word_string:
        if char.isdigit():
            return False
        elif char.isspace():
            return False
        elif SPECIAL.find(char)>=0:
            return False
        else:
            return True

while is_valid_format(word_string) == True:
    word = ""

    for kind in word_string:
        if kind == "#":
            word += random.choice(VOWELS)
        elif kind == "%" or kind == "*":
            word += random.choice(CONSONANTS)
        else:
            word += kind
    print(word)







