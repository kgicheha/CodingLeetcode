'''
STEPS:
1. splits array in half
2. Call Merge Sort on each half to sort them recursively
3. Merge both sorted halves into one sorted array
4.

TIME Comlexity: O(n log n)
Space Complexity: O(1)
'''

def mergeSort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftArr = arr[:mid]
    rightArr = arr[mid:]

    # recursion on the left and right array
    mergeSort(leftArr)
    mergeSort(rightArr)

    merge_two_sorted_lists(leftArr, rightArr, arr)


def merge_two_sorted_lists(a,b, arr):

    len_a = len(a)
    len_b = len(b)


    i = 0   #left_arr index
    j = 0   #right array index
    k = 0   #index at merged array

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1

        else:
            arr[k] = b[j]
            j += 1

        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


    print(arr)

arr = [3,2,6,7,1,2,4]
mergeSort(arr)


