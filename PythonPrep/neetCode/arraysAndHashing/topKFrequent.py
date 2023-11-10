import heapq

def topKFrequent(nums, k):
    result = []
    numCountDict = {}

    for i in range(len(nums)):
        if nums[i] not in numCountDict:
            numCountDict[nums[i]] = 0

        numCountDict[nums[i]] += 1

    print(numCountDict)
    heap = []
    for key,value in numCountDict.items():
        heap.append([value, key])

    print(heap)
    heapq.heapify(heap)
    print("Heap", heap)

    while len(heap) > k:
        heapq.heappop(heap)

    print("Popped Heap", heap)
    for freq, value in heap:
        result.append(value)

    return result
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
'''
Link: https://leetcode.com/problems/top-k-frequent-elements/
'''

'''
GIVEN:
    array of integers
    integer
STEPS:
    import heapq

    create empty dictionary
    initialize empty array to store the results

    iterate through given array:
        if the number is in dictionary:
            increment count by 1

        add it to the dictionary with 0 as its count

    intialize an empty array that will be used to be heapify/priority sort

    iterate though the Dictionary:
        store the values and keys, in that order, to the empty array
            this is because the heapq.heapify will sort based on the first value,
                and since we want to stor by the frequency, we have to place it as the first value


    heapfity the array --> in other words, sort the array

    iterate through the array, while the length is > k:
        pop/remove the last element of the array

    iterate though the array again:
        append the value to the results array

    return the results array


    return result array
RESULT:


'''