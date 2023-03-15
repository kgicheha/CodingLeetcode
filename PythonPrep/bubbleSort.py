'''
Works by repeatedly swapping the adjacent elements
if they are in  the wrong order.

'''

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr
arr = [3,2,1,5,7]
print(bubbleSort(arr))