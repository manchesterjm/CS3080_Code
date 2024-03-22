def num_chkr(num_list) :
    for j in range(0, len(num_list)-3) :
        if num_list[j] == num_list[j+1] and num_list[j] == num_list[j+2] :
            return True
    return False

list_1 = [-4, 9, 9, 9, 3, 8]
list_2 = [5, 3, 3, 7, 7, -2, -2]
list_3 = [12, 12, 12, 12, 5, 5, 5, 2, 2]

print(num_chkr(list_1))
print(num_chkr(list_2))
print(num_chkr(list_3))