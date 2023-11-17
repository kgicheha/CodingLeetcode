def majorityElement(nums):

    # STRATEGY 2
    res = 0
    count = 0

    for i in range(len(nums)):
        if count == 0:
            res = nums[i]

        if nums[i] == res:
            count += 1
        else:
            count -=1

    return res

    # STRATEGY 1
    # threshold = len(nums) // 2

    # intCount = {}

    # for i in range(len(nums)):
    #     if nums[i] in intCount:
    #         intCount[nums[i]] += 1

    #     else:
    #         intCount[nums[i]] = 1

    # for i in intCount:
    #     if intCount[i] > threshold:
    #         return int(i)

nums = [3,2,3]
print(majorityElement(nums))

'''
GIVEN:
    array of integers
STEPS:
    # SOLUTION 1: TIME and SPACE Complexity: O(n)

        threshold = len(array) // 2

        intCount = {}

        iterate through given array:
            if current number in intCount hashMap:
                increment the count by 1

            else:
                add the number to the hashmap with a value of 1


        if any value in the hashap is > than threshold:
            return its key


    SOLUTION 2: TIME COMPLEXITY: O(n), SPACE COMPLEXITY: O(1)

        intialize result equal to 0
        initialize count = 0

        for i in range(len(array)):
            if count == 0:
                assign the current number to the result

            if current number == result:
                increment count by 1
            else:
                decrement count by 1

        return result
RESULTS:
    return the majority element
        majority element appears > len(array) / 2

'''