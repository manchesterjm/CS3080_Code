from random import randint

def rtn_rnd(a) :
    return a[randint(0, len(a) -1)]

list_1 = [5,-9,70,15]
list_2 = [0,1,2,3,4,7,12]

print(rtn_rnd(list_1))
print(rtn_rnd(list_2))