def dup_chk(a) :
    a = a.lower()
    dict1 = {}
    for i in a: dict1[i] = dict1.get(i, 0) + 1
    print(*(key for key in dict1 if dict1[key] >= 2), end=' ')
    print('')

string_1 = "hello"
string_2 = "abcCdbB"
string_3 = "abcdefghiJKL"

dup_chk(string_1)
dup_chk(string_2)
dup_chk(string_3)