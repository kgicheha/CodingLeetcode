'''
Question Link:
https://www.algoexpert.io/questions/first-duplicate-value

'''
'''
GIVEN:
    an array of integers
STEPS:
    initialize empty set

    traverse given array:
        if current number is not in the set:
            add it to the set
        else:
            return the current number
RESULT:
    return the number whose first diplicate value has the minimum value
    else:
        return -1

'''

def firstDuplicateVale(array):

    print(array)

array =[2, 1, 5, 2, 3, 3, 4]