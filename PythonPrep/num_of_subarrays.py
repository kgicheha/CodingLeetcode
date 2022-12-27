'''
Given an array of integers arr and two integers k and threshold,
return the number of sub-arrays of size k
and average greater than or equal to threshold.
'''

'''
EXAMPLE
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8]
have averages 4, 5 and 6 respectively.
All other sub-arrays of size 3 have averages
less than 4 (the threshold).
'''

'''
PSUEDOCODE
1. Find the sum of the first k units
2. Find the avg of the k units
    avg = sum / k
3. If the average of sum over k is equal to or greater than the threshold.
    increment count by 1
4. For the rest of the array:
    a. Slide window up by 1 element
    b. Calculate the average of these k elements
    c. If the average of sum over k is equal to or greater than the threshold.
        increment count by 1
5. Return counter


TIME COMPLEXITY = O(n)
SPACE COMPLEXITY = O(1)

'''
def num_of_subarrays(arr, k, threshold):

    sum_of_values = 0
    count = 0
    avg = 0

    current_index = 0
    while(current_index < k):
        sum_of_values += arr[current_index]
        current_index += 1

    avg = int(sum_of_values / k)
    if(avg >= threshold):
        count +=1

    left_pointer = 1
    right_pointer = k
    while(right_pointer < len(arr)):
        # subract the value of the previous left pointer from sum
        sum_of_values -= arr[left_pointer - 1]
        # add the value of the new right pointer
        sum_of_values += arr[right_pointer]

        avg = int(sum_of_values / k)
        if(avg >= threshold):
            count +=1

        left_pointer += 1
        right_pointer += 1

    print(count)

arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
num_of_subarrays(arr, k, threshold)
