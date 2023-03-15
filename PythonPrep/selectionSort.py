'''
Repeatedly find the index minimum element
Use the index to move the minimum element to the
sorted part of array
Then we repeat the process for each of the remaining elements in the
unsorted list. The next element entering the sorted list is compared
with the existing elements and placed at its correct position.
So at the end all the elements from the unsorted list are sorted.
Takes O(n^2) time complexity and O(1) space

'''
def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i

        for j in range(i+1, len(arr)):
            if arr[j] < minIndex:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr


arr = [3,1,-1,5,2]
print(selectionSort(arr))