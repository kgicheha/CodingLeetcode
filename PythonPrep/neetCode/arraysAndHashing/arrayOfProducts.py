def arrayOfProducts(array):

    product = 1

    leftArray = [1] * len(array)

    for i in range(len(array)):
        leftArray[i] = product
        product *= array[i]

    print(leftArray)

    product = 1
    rightArray = [1] * len(array)

    for i in range(len(array)-1, -1, -1):
        rightArray[i] = product
        product *= array[i]

    print(rightArray)

    res = []

    for i in range(len(array)):
        res.append(leftArray[i] * rightArray[i])

    return res

# def arrayOfProducts(array):

    # BRUTE FORCE
#     res = []
#     for i in range(len(array)):
#         curProduct = 1

#         for j in range(len(array)):
#             if i != j:
#                 curProduct *= array[j]

#         res.append(curProduct)

#     return res


array = [5, 1, 4, 2]
# [8, 40, 10, 20]
print(arrayOfProducts(array))

'''
GIVEN:
    An array of integers.
STEPS:
    # STRATEGY 1 (BRUTE FORCE): O(n^2)

        initialize result equal to empty array list

        create for loop for i:
            initialize current Product to 1

            create another for loop inside for j:
                if i != j:
                    multiply the value at index j with current product
                    assign it back to current product

            append the product to the result array list

        return the result array


    # STRATEGY 2: TIME and SPACE COMPLEXITY: O(n)

        initialize product equal to 1

        initalize leftArray list to the length of given array

        iterate through given array from left to right:
            at every integer:
                add the product to the left Array at its respective index
                multiply the product by the integer


        reset the product array back to 1

        initialize right Array to the length of the given array

        iterate through given array in reverse order: --> from right to left
            at every integer:
                add the product to the right Array at its respective index
                multiply the product by the integer


        initalzie empty result array list

        iterate through given array list:
            at each index:
                multiply both the numbers that are the same index from the left and right arrays

                append the answer to the result array list

        return the result array


    #
    input Array = [5, 1, 4, 2]

    leftProductArray = [1]
    leftProductArray = [1, 5]
    leftProductArray = [1, 5, 5]
    leftProductArray = [1, 5, 5, 20, 40]

    input Array = [5, 1, 4, 2]

    rightProductArray =[1]
    rightProductArray =[2, 1]
    rightProductArray =[8, 2, 1]
    rightProductArray =[8, 8, 2, 1]
    rightProductArray =[40, 8, 8, 2, 1]


'''

