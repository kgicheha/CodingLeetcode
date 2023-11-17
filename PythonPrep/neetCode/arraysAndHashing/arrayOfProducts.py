def arrayOfProducts(array):

    # STRATEGY 3: O(N)
    res = [1] * len(array)

    product = 1
    for i in range(len(array)):
        res[i] = product
        product *= array[i]

    print(res)
    product = 1
    for i in range(len(array)-1, -1, -1):
        res[i] *= product
        product *= array[i]
    print(res)



# def arrayOfProducts(array):

#     # SOLUTION 2
#     product = 1

#     leftArray = [1] * len(array)

#     for i in range(len(array)):
#         leftArray[i] = product
#         product *= array[i]

#     print(leftArray)

#     product = 1
#     rightArray = [1] * len(array)

#     for i in range(len(array)-1, -1, -1):
#         rightArray[i] = product
#         product *= array[i]

#     print(rightArray)

#     res = []

#     for i in range(len(array)):
#         res.append(leftArray[i] * rightArray[i])

#     return res

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


    # STRATEGY 3: TIME Complexity: O(n), Space Complexity: O(1)

        initialize result array equalt to the length of the given array

        initalize product equal to 1

        iterate through given array: from left to right
            at each index:
                append the product to the result array at its corresponding index in the
                multiply product by the number at the current index


        reset product equal to 1

        iterate through given array in reverse order:
            at each index:
                multiply the current number with the number that in the same index in the result array
                multiply the current number with the product


'''

