# DOCSTRING
def sortDict(dict1):
    keys = dict1.keys() # Taking the keys of dictionary
    keys = list(map(int, keys))
    keys.sort() # Sorting the keys
    keys = list(map(str, keys))
    dict_copy={}

    # For sorted dictionary
    for i in keys:
        dict_copy[i] = dict1[i]
    return dict_copy

# Returns the values from position first, second, last and second last
def position(dict1):
    keys = list(dict1.keys())
    vals = []
    vals.append(dict1[keys[0]])
    vals.append(dict1[keys[1]])
    vals.append(dict1[keys[-1]])
    vals.append(dict1[keys[-2]])
    return vals

# Concatenates the values obtained keys in a string
def concat(arr):
    strg = ' '.join(arr)
    return strg

# Joins the first and last character of each word(no spaces)
def join(strg):
    arr = strg.split(" ") # Splits the string into array of each word seperated by spaces.
    ar = []
    for i in arr: #List comprehension ADD!!!!
        ar.append(i[0] + i[-1])
    joinString = "".join(ar)
    return joinString

# Calculates the occurance of each letter and returns the top 5 letters with their occurance.
def occurance(joinString):
    joinString = joinString.lower()
    dict1 = {}
    for i in joinString:
        if i == '.' or i == ',': # Doesnt include . or ,
            continue
        else:
            if i in dict1.keys():
                dict1[i] += 1
            else:
                dict1[i] = 1
    vals2 = list(dict1.items())
    vals2.sort(key= lambda x: x[1], reverse=True) # Sorts in descending order of the values of occurance.
    dict_copy={}
    for i,_ in vals2[0:5]:
        dict_copy[i]= dict1[i]
    vals1 = list(dict_copy.values())
    return dict_copy, vals1 # Returns dictionary of letters(keys) and occurance(values), and array of occurance alone.

# Adds the key list with the occurance list.
def addKey(key_list, arr):
    addArr= []
    for i in range(len(arr)):
        addArr.append(key_list[i]+arr[i])
    return addArr

# Converts the list of decimal values into corresponding ASCII values
def asc(arr):
    finalArr = []
    for i in arr:
        finalArr.append(chr(i))
    return finalArr