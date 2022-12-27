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
2. Add to counter if the avergae of sum over k is equal to or greater than the threshold.
3. For the rest of the array:
    a. Slide window up by 1 element
    b. Calculate the average of these k elements
    c. if the k element's average is greate than the threshold,
        add to the counter
4. Return counter

'''
def num_of_subarrays():
