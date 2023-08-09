'''
Question Link: algoexpert.io/questions/class-photos

'''
'''
GIVEN:
    2 arrays of heights
STEPS:
    1. sort the given array in descending order, destructively
    2. compare the values at the beginning of each array.
        if the value of RedShirt Array is less than the value of the BlueShirt array:
                the redshirt Array will be the 1st row

    3. loop through the two sorted array
        compare each value

        if the RedShirt array is the 1st row:
            if the value at each index is MORE or EQUAL TO the value of blueShirt at the same index:
                return False --> the arrangement doesnt fit the rules
        else if the BLUEShirt array is the first row:
            if the value at current index is MORE OR EQUAL TO the value of the REDSHIRT height at the same index:
                return False --> the arragement doesn't fit the rules


    return True --> meaning the loop have gone through successfully


RESULT:
    returns True if the photo follows the stated guideline
    else return False if you cant take the photo due to not having the proper guideline

TIME COMPLEXITY --> 0(nlogn) because we have to sort the given arrays
SPACE COMPLEXITY --> 0(1) because we dont have to create new arrays
'''


def classPhotos(redShirtHeights, blueShirtHeights):

    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    shirtColorInFrontRow = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'

    for idx in range(len(redShirtHeights)):
        currrentRedShirtHeight = redShirtHeights[idx]
        currentBlueShirtHeight = blueShirtHeights[idx]

        if shirtColorInFrontRow == 'RED':
            if currrentRedShirtHeight >= currentBlueShirtHeight:
                return False
        else:
            if currentBlueShirtHeight >= currrentRedShirtHeight:
                return False

    return True




redShirtHeights = [5,8,1,3,4]
blueShirtHeights = [6,9,2,4,5]
print(classPhotos(redShirtHeights, blueShirtHeights))

# red_decrement_order = [8,5,4,3,1]
# blue_decrement_order = [9,6,5,4,2]

