'''
Given an array with integers,
return the sum of the subarray with the largest sum.
'''

'''
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The maximum sum subarray goes from index 3 to index 6 with a total sum of 6.
'''
'''
BRUTE FORCE APPROACH
    initiliaze the max sum variable and set it equal to the first element in the given arrya

    loop through each index
        initialize a variable that keep track of the current sum in each index

        in each index, add the the rest of the elements in the array

            compare the sum with the max sum variable
            if the current sum is more than the max sum variable,
                set the current sum as the max sum variable

    TIME COMPLEXITY: 0(N^2)
    SPACE COMPLEXITY: 0(1)

OPTIMAL SOLUTION (KADANE'S ALGORITHM --> DYNAMIC PROGRAMMING)

'''


def maxSumSubarray(arr):
    n = len(arr)

    # BRUTE FORCE APPROACH
    # max_sum = arr[0]

    # for left in range(n):
    #     cur_sum = 0
    #     for right in range(left, n):
    #         cur_sum += arr[right]

    #         max_sum = max(max_sum, cur_sum)

    # print(max_sum)

    # OPTIMAL SOLUTION
    max_sum = arr[0]
    cur_sum = arr[0]

    for i in range(1, n):
        cur_sum = max(arr[i] + cur_sum, arr[i])

        max_sum = max(cur_sum, max_sum)
    print(max_sum)



arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSumSubarray(arr)