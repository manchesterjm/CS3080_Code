def char_count(a) :
    count = sum(1 for i in a if not i.isspace())
    print(count)
    
char_count(input("Please, enter a word : "))