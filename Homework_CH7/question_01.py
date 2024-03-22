'''
Write program that matches a string that contains sequences of lowercase
letters joined by an underscore
'''

# Need to look for _
# Need to look for Upper Case
# if no _ or there are Upper Case, then fail

import re

def str_chkr(a) :
    return bool(re.search("^[a-z_]*$", a)) # need the whole string to match this pattern
                                           # from start "^" only _ and only lower case "*" repeating to end "$"
        
input_1 = 'aab_cbbbc'
input_2 = 'aab_Abbbc'
input_3 = 'Aaab_abbbc'

print(str_chkr(input_1))
print(str_chkr(input_2))
print(str_chkr(input_3))