def insertionSort(arr):

    for i in range(1, len(arr)):

        while arr[i - 1] > arr[i] and i > 0:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]

            i = i - 1

    return arr
arr = [-1,-2,3,1,4,2,5]
print(insertionSort(arr))