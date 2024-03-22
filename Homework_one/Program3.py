intNum = int(input('Please, enter the value of n: '))
if intNum <= 0 :
    print('Invalid Input')
else :
    for i in range(0, intNum) :
        for j in range(0, intNum - i) :
            print('* ', end = '')
        print()