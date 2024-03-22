userinput = input('enter you name : ')
print('your name will be right justified 5 spaces')
x = len(userinput)
print(userinput.rjust(5 + x, '*'))