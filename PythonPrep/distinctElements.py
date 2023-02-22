'''
Given an integer array, print all maximum size subarrays
having all distinct elements in them.
'''

'''
GIVEN:
    array of integers
STEPS:
    initi
    initiliaze variable that keeps track of max

    loop through given array:


RESULT:
    print out all the max size subarray with distict elements in them
'''
def distinctElements(arr):

    left, right = 0, 0
    max_so_far = 0

    seen = set()

    while right < len(arr):

        while right < len(arr) and (arr[right] not in seen):
            seen.add(arr[right])
            right += 1

        cur_window = arr[left:right]
        print("current window", cur_window)

        while right < len(arr) and (arr[right] in seen):
            seen.remove(arr[left])
            left += 1

arr = [5, 2, 3, 5, 4, 3]
distinctElements(arr)

'''
STEPS:
    initialize variable
    intialize current window size
    initiliaze variable that keeps track of max

    loop through given array:
        if current element is not in set:
            increment window size by 1 index
            compare between the previous max to the current window size
                if current window size is more that previous max
                    add the elements in the current window size
        else:
            reset the window size back to 0 by setting left pointer equal to right

        add current element to set



 left, right = 0,0
    max_so_far = 0

    seen = set()


    for i in range(len(arr)):

        if arr[i] not in seen:
            right += 1

        elif arr[i] in seen:

            print(seen)
            cur_window = arr[left:right]

            if len(cur_window) >= max_so_far:
                print(cur_window)
                max_so_far = max(max_so_far, len(cur_window))


            seen.remove(arr[i - right])

            left += 1
            max_so_far += 1

        seen.add(arr[i])
'''