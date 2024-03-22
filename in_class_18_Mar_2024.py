import math, openpyxl

#print(openpyxl.__version__)
'''
def is_prime(num) :
    if num < 2 :
        return False
    for i in range(2, math.ceil(math.sqrt(num))+1) :
        if num % i == 0 :
            return False
    return True
'''

wb_one = openpyxl.load_workbook('test.xlsx')
print(wb_one.sheetnames)