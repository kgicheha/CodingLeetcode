'''
STEPS:
1. splits array in half
2. Call Merge Sort on each half to sort them recursively
3. Merge both sorted halves into one sorted array
4.

TIME Comlexity: O(n log n)
Space Complexity:
'''

def mergeSort(arr):
    print(arr)





def merge_two_sorted_lists(a,b):
    sorted_list = []

    len_a = len(a)
    len_b = len(b)


    i = j = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[j])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1


    return sorted_list

arr = [3,2,6,7,1,2,4]
mergeSort(arr)