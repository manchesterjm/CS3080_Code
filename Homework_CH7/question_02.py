'''
Write a Python program to search for a sequence of one upper-case letter
followed by a lower-case one.
'''

# "search" for a pattern of Upper then lower
# only needs to occur once

import re

def checker(a) :
    return bool(re.search('[A-Z][a-z]', a))

input_1 = 'AaBbGg'
input_2 = 'Python'
input_3 = 'python'
input_4 = 'PYTHON'
input_5 = 'aA'
input_6 = 'Aa'

print(checker(input_1))
print(checker(input_2))
print(checker(input_3))
print(checker(input_4))
print(checker(input_5))
print(checker(input_6))