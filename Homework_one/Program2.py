'''
The algorithm to determine if a year is a leap year is as follows:
Every year that is exactly divisible by four is a leap year, except
for years that are exactly divisible by 100, but these centurial
years are leap years, if they are exactly divisible by 400.
'''
input_year = int(input('Please, enter the (in YYYY format): '))
if input_year % 100 == 0 :
    if input_year % 400 == 0 :
        print('This is a leap year')
    else :
        print('This is not a leap year')
elif input_year % 4 == 0 :
    print('This is a leap year')
else :
    print('This is not a leap year')