def bubbleSort(lst):
    for i in range(len(lst)-1):
        for j in range(0,len(lst)-i-1):
            if lst[j+1]<lst[j]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst


def sortDict(dict1):
    '''Takes dictionary as input and returns sorted dictionary'''
    keys = dict1.keys() # Taking the keys of dictionary
    keys = list(map(int, keys))
    keys = bubbleSort(keys) # Sorting the keys
    keys = list(map(str, keys))
    dict_copy={}

    # For sorted dictionary
    for i in keys:
        dict_copy[i] = dict1[i]
    return dict_copy

def position(dict1):
    '''Returns the values from position first, second, last and second last'''
    keys = list(dict1.keys())
    vals = []
    vals.append(dict1[keys[0]])
    vals.append(dict1[keys[1]])
    vals.append(dict1[keys[-1]])
    vals.append(dict1[keys[-2]])
    return vals

def concat(arr):
    '''Concatenates the values obtained keys in a string'''
    strg = ' '.join(arr)
    return strg

def join(strg):
    '''Joins the first and last character of each word(no spaces)'''
    arr = strg.split(" ") # Splits the string into array of each word seperated by spaces.
    ar = [x[0]+x[-1] for x in arr]
    joinString = "".join(ar)
    return joinString

def occurance(joinString):
    '''Calculates the occurance of each letter and returns the top 5 letters with their occurance.'''
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

def addKey(key_list, arr):
    '''Adds the key list with the occurance list.'''
    addArr= []
    for i in range(len(arr)):
        addArr.append(key_list[i]+arr[i])
    return addArr

def asc(arr):
    '''Converts the list of decimal values into corresponding ASCII values'''
    finalArr = [chr(i) for i in arr]
    return finalArr