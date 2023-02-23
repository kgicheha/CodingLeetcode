'''
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant
in left-to-right order.
The large integer does not contain any leading 0's.
'''

'''
EXAMPLE:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
'''

'''
GIVEN:
    arry of digits
STEPS:
    initiliaze right pointer equal to the last element in the given array
    initialize carryOver varaible to 1
        since we're incrementing the value by 1

    while right pointer is >= 0:
        intiliaze a temp variable that stores the sum of the current element and 1

        if the temp variable is more that 9:
            set the current element equal to 0
        else:
            set the current element equal to the temp variable

        decrement right pointer by 1

    if the carryOver is still equal to 1 after you break out of while loop:
        this means that they you're still left with the carry over
        insert the carry over to the beginning of the given array

    return the array
RESULT:
    return the given array after incrementing it by 1

'''
def plusOne(digits):

    right  = len(digits) -1
    carry_over = 1

    while right >= 0:

        temp = digits[right] + carry_over

        if temp> 9:
            digits[right] = 0
        else:
            digits[right] = temp
            carry_over = 0

        right -= 1

    if carry_over == 1:
        digits.insert(0,carry_over)

    print(digits)


digits = [1,9,9,9]
plusOne(digits)
