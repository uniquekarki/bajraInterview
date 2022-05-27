from base import *

def sortDict(dict1):
    keys = dict1.keys()
    keys = list(map(int, keys))
    keys.sort()
    keys = list(map(str, keys))
    dict_copy={}
    for i in keys:
        dict_copy[i] = dict1[i]
    return dict_copy

def position(dict1):
    keys = list(dict1.keys())
    vals = []
    vals.append(dict1[keys[0]])
    vals.append(dict1[keys[1]])
    vals.append(dict1[keys[-1]])
    vals.append(dict1[keys[-2]])
    return vals

def concat(arr):
    strg = str(arr[0] + ' '  + arr[1] + ' ' + arr[2] + ' ' + arr[3])
    return strg

def join(strg):
    arr = strg.split(" ")
    ar = []
    for i in arr:
        ar.append(i[0] + i[-1])
    joinString = "".join(ar)
    return joinString

def occurance(joinString):
    joinString = joinString.lower()
    dict1 = {}
    for i in joinString:
        if i == '.' or i == ',':
            continue
        else:
            if i in dict1.keys():
                dict1[i] += 1
            else:
                dict1[i] = 1
    vals2 = list(dict1.items())
    vals2.sort(key= lambda x: x[1], reverse=True)
    dict_copy={}
    for i,_ in vals2[0:5]:
        dict_copy[i]= dict1[i]
    vals1 = list(dict_copy.values())
    return dict_copy, vals1

def addKey(key_list, arr):
    addArr= []
    for i in range(len(arr)):
        addArr.append(key_list[i]+arr[i])
    return addArr

# question 1
chest = sortDict(chest)

# question 2
vals = position(chest)

# question 3
strg = concat(vals)
# print(strg)

# question 4
joinString = join(strg)
# print(joinString)

# question 5
dict1, occur = occurance(joinString)
print(dict1)
print(occur)

# question 7
addArr = addKey(key_list, occur)
print(addArr)

# question 8
finalArr = []
for i in addArr:
    finalArr.append(chr(i))
print(finalArr)
