# Performing string manipulation with string methods and functions

import string

text = input("Enter a sentence: ")

print("Length: ", len(text))
print("No Space: ", text.strip())
print("Upper:  ", text.upper())
print("Lower:  ", text.lower())
print("Words:  ", text.split())
print("Reversed: ", text[::-1])
print("AlphaNumeric: ", text.isalpha())
