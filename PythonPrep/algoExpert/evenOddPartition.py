def evenOddPartition(array):

    even = []
    odd = []

    for i in range(len(array)):
        if array[i] % 2 == 0:
            even.append(array[i])
        elif array[i] % 2 != 0:
            odd.append(array[i])

    return even + odd


array = [89, 91, 30, 57, 72, 89, 90]

print(evenOddPartition(array))

'''
GIVEN:
    array of integers
STEPS:
    STRATEGY 1: Time and Space Complexity O(n)
        initialize 2 empty array lists,
            1 will store the even number, the other will store the odd numbers


        iterate through given array:
            if the current number / 2 has no remainder left:
                append it to the list of even numbers
            elif the current number / 2 has a remainder left:
                append it to to the list of odd numbers

        return even + odd


    initialize left and right pointer to 0 and len(array) - 1, respectively

    iterate given array while left pointer <= right pointer:
        if number at the left index is odd:
            swap the number at the left index with the number at the right index
            decrement the right pointer by 1

        elif the number at the right pointer is even:
            swap the number at the left index with the number at the right index
            increment the left pointer by 1

    return array
RESULTS:
    return the array with all the even numbers in the left half of the array.
        and all the odd numbers in the right half of the array
'''