'''
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2,
return an array of their intersection.
Each element in the result must be unique
and you may return the result in any order.
'''

'''
EXAMPLE 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
'''

'''
GIVEN: 2 arrays
STEPS:
    create a variable that stores the set of nums1 array
    create a variable that stores the set of nums2 array

    SOLUTION 2:
    use LIST function to return the integers that are in both set of nums1 and set of sums2
RESULT:
    an array of their intersection

TIME AND SPACE COMPLEXITY O(n+m)
'''

def intersection(nums1, nums2):

    set1 = set(nums1)
    set2 = set(nums2)

    # SOLUTION 1

    res = []
    for i in nums2:
        if (i in set1) and (i not in res):
            res.append(i)
    return res


    # SOLUTION 2

    # return list(set1 & set2)




nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersection(nums1, nums2))