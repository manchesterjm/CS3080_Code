import re

def find_pat(string, pat) :
    a = re.search(pat, string)
    return a
    
patrn = r"\w*ring\w*"
test = "this is a tent string with a prize in it and it is the best"

print(find_pat(test, patrn))
print(bool(find_pat(test, patrn)))