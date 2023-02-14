'''
Find the minimum number of swaps required
to sort the array in ascending order.
'''

def minimumSwaps(arr):
    swapCount = 0
    minSwap = 0

    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                swapCount += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        # minSwap = min()
    print(arr)
    print(swapCount)

# arr = [7,1,3,2,4,5,6]
arr = [4,3,1,2]
minimumSwaps(arr)