def csIsomorphicStrings(a, b):
    
    letters = {}
    newWord = ""
    
    if len(a) != len(b):
        return False
    
    for i, letter in enumerate(a):

        if letter not in letters:
            letters[letter] = b[i]
        
        newWord += letters[letter]
        
    if newWord == b:
        return True
    else:
        return False         
    
'''

U:

a = "abba"
b = "cddc"
output = True

a = "llama"
b = "dress"
output = False

P:

create new dict latters; set a's values to keys and b's values to values.  If a translated to values is equal to b, return True; otherwise, return False

'''

# ===============

