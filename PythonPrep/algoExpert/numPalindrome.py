def numPalindrome(x):

    if x < 0:
        return False

    if x >=0 and x< 10:
        return True

    stringVersion = str(x)


    lp = 0
    rp = len(stringVersion) - 1

    while lp <= rp:
        if stringVersion[lp] != stringVersion[rp]:
            return False

        lp += 1
        rp -= 1

    return True

x= 12321
print(numPalindrome(x))
'''
GIVEN:
    an integer
STEPS:
    change integer to string

    create left and right pointers equal to 0, last index, respectively

    iterate through string:
        if value at left pointer != value at right pointer:
            return False
        else:
            increment left pointer
            decrement right pointer

    return True



RESULTS:
    return True if the number is a palidrome:
        meaning it can be written the same way back and forth

    else:
        return False
'''