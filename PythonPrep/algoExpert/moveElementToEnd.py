'''
Question Link:
https://www.algoexpert.io/questions/move-element-to-end
'''

'''
GIVEN:
    an array of integers
    an integer
STEPS:

    # sort given array
    initialize 2 pointer
        1st pointer starts at 0
        2nd pointer starts at last element

    traverse given array





RESULT:
    return a mutated array with the given integer at the end
    HAVE TO PERFORM THIS IN PLACE
'''

def moveElementToEnd(array, toMove):
    print(array)

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2



'''
traverse sorted array
        once you get to the first appearance of the given integer:
            place pointer there
            increase the size of the window until you get to the last appearance of the given integer

            slice the window out of the array
            store the rest of the integers in one variable
            store the window of the given integer in another variable
'''