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

def csWordPattern(pattern, a):
    
    patDict = {}
    a_2 = a.split(" ")
    newStr = ""
    newList = []
    count = 0
    
    if len(a_2) != len(pattern):
        return False
    
    for i, letter in enumerate(pattern):
        
        if letter not in patDict:
            patDict[letter] = a_2[i]
            
            count += 1
            
        if patDict[letter] not in newList:
            newList.append(patDict[letter])
        
        if i == len(a_2)-1:
            newStr += patDict[letter]
        else:
            newStr += patDict[letter]
            newStr += " "
            
    if count != len(newList):
        return False
        
    if newStr == a:
        return True
    else:
        return False
    
    
    
'''

U:

pattern = "abba"
a = "lambda school school lambda"
output = True

P:

create dictionary patDict; key = pattern("a"), value = a("lambda"); iterate through pattern, putting coresponding value into newStr.  if newStr = a, return True, otherwise, return False

'''

# ===============

def csGroupAnagrams(strs):
    
    str = set("".join(strs))
    
    letters = {}
    sums = {}
    newList = []
    
    for i, letter in enumerate(str):
        if letter not in letters:
            letters[letter] = 2**i
            
    for j in strs:
        sum = 0
        for l in j:
            sum += letters[l]
            
        if sum not in sums:
            sums[sum] = [j]
        else:
            sums[sum].append(j)
            
    for key in sums.values():
        newList.append(key)
        
    return newList