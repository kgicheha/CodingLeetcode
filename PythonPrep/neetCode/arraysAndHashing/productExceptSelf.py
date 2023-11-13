def productExceptSelf(nums):

    # STRATEGY 1
    # product = 1
    # res = []

    # for num in nums:
    #     product *= num

    # for num in nums:
    #     curProd = int(product / num)
    #     res.append(curProd)

    # return res

    preFixArray =[]
    preFixArray.insert(0, 1)

    preFixIdx = 1

    for i in range(len(nums)):
        currProd = nums[i] * preFixArray[preFixIdx-1]
        preFixArray.append(currProd)
        preFixIdx += 1

    print(preFixArray)


    postFixArray = []
    postFixArray.insert(0,1)

    for i in range(len(nums)-1, -1, -1):
        curProd = nums[i] * postFixArray[0]
        postFixArray.insert(0, curProd)

    print(postFixArray)

    res = []

    for i in range(len(nums)):
        finalProd = preFixArray[i] * postFixArray[i+1]
        res.append(finalProd)

    return res


nums = [1,2,3,4]
# Output: [24,12,8,6]
print(productExceptSelf(nums))
'''
Link: https://leetcode.com/problems/product-of-array-except-self/
'''
'''
GIVEN:
    array of numbers
STEPS:
    STRATEGY 1: TIME and SPACE Compl: O(n)
        initialize variable that keeps track of products to 1
        initialize results array

        iterare through given array:
            mupltiple current product value by the current number
            update the product value

        iterate through given array
            divide the product value by the current number
            append the output to the results array

        return the results array



    STRATEGY 2:


RESULTS:
    array of products of all numbers except for the nums[i]

'''