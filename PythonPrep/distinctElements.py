'''
Given an integer array, print all maximum size subarrays
having all distinct elements in them.
'''

'''
GIVEN:
    array of integers
STEPS:

    initialize variable left and right pointers to 0
    initiliaze variable that keeps track of max length to 0
    initilize empty arry that'll be used to sotre the max subarry
    initilize  empty set that will be used to store each element


    loop through given arry
        while the right pointer is less the length of array AND the current element in not in set:
            add the element to the set
            increment right pointer by 1
                this will increase the size of the window

        store the window from the left pointer to the where the right pointer currently is

        if the length of the window is >= max length that we've seen so far:
            set the length of the window as the new max length
            store the window to the max subarry variable

        while right pointer is less than the length of array AND the current element is in the set:
            remove the item from the set
            increment left pointer by 1
                this will reduce the size of the window

        return the max size window variable


RESULT:
    print out all the max size subarray with distict elements in them
'''
def distinctElements(arr):

    left, right = 0, 0
    max_so_far = 0
    max_size_window = []

    seen = set()

    while right < len(arr):

        while right < len(arr) and (arr[right] not in seen):
            seen.add(arr[right])
            right += 1

        cur_window = arr[left:right]

        if len(cur_window) >= max_so_far:
            # print("current window", cur_window)
            max_so_far = max(max_so_far, len(cur_window))
            max_size_window = cur_window

        while right < len(arr) and (arr[right] in seen):
            seen.remove(arr[left])
            left += 1

    print(max_size_window)


arr = [5, 2, 3, 5, 4, 3]
distinctElements(arr)
