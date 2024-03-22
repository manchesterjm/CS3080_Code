import math
def up(a) :
    mid = math.ceil(len(a) / 2)
    a = a[:mid] + a[mid:].upper()
    print(a)
    
test = input("Please, enter a word : ")

up(test)