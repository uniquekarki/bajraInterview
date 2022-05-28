from base import *
from func import *
import json # Only for printing the dictionary in presentable format.



if __name__ == '__main__':
    # question 1
    chest = sortDict(chest)
    print('\n-----------------------------OUESTION 1-----------------------------')
    print('Sorted dictionary:\n')
    print(json.dumps(chest, indent=4))

    # question 2
    vals = position(chest)
    print('\n-----------------------------OUESTION 2-----------------------------')
    print('The values of first, second, last and second last values of dictionary:\n',vals)

    # question 3
    strg = concat(vals)
    print('\n-----------------------------OUESTION 3-----------------------------')
    print('The string after concatinating the desired values:\n',strg)

    # question 4
    joinString = join(strg)
    print('\n-----------------------------OUESTION 4-----------------------------')
    print('The string after joining first and last letters:',joinString)
    
    # question 5
    dict1, occur = occurance(joinString)
    print('\n-----------------------------OUESTION 5-----------------------------')
    print('Top 5 occured letters with occurance:\n')
    print(json.dumps(dict1, indent=4))
    # print(dict1)
    print('Top 5 occurance:',occur)

    # question 6
    print('\n-----------------------------OUESTION 6-----------------------------')
    print('The key list is:', key_list)

    # question 7
    addArr = addKey(key_list, occur)
    print('\n-----------------------------OUESTION 7-----------------------------')
    print('The list after adition is:',addArr)

    # question 8
    finalArr = asc(addArr)
    print('\n-----------------------------OUESTION 8-----------------------------')
    print(finalArr)
    strgFinal = ''.join(finalArr)
    print(f'Final string is: "{strgFinal}"')