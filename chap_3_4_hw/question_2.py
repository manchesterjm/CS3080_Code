def merge_list(a, b) :
    temp_list = a + b
    temp_list.sort()            
    return(temp_list)

list_1 = [1,3,5,7]
list_2 = [2,4,6,8]
list_3 = [0,7,9,12]
list_4 = [0,1,2,3,4,7,12]

print(merge_list(list_1, list_2))
print(merge_list(list_3, list_4))