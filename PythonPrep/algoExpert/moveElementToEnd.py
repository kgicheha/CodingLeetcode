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

        if current value is EQUAL to given integer and current value is not equal to the integer at the 2nd pointer:
            swap the two values
            increment lp by 1

        elif currentvalue == given integer and current value is equal to value at the right pointer:
            decrement right pointer by 1

        elif currentValue != given integer:
            increment left pointer by 1

RESULT:
    return a mutated array with the given integer at the end
    HAVE TO PERFORM THIS IN PLACE
'''

def moveElementToEnd(array, toMove):
    print(array)

    lp = 0
    rp = len(array) - 1

    while lp < rp:

        if array[lp] == toMove and array[lp] != array[rp]:
            temp = array[lp]
            array[lp] = array[rp]
            array[rp] = temp
            lp += 1
        elif array[lp] == toMove and array[lp] == array[rp]:
            rp -= 1
        elif array[lp] != toMove:
            lp += 1

    return array

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
print(moveElementToEnd(array, toMove))
