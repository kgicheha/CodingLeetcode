'''
Repeatedly find the minimum element and move it to the
sorted part of array to make unsorted part sorted (in ascending order)
Then we repeat the process for each of the remaining elements in the
unsorted list. The next element entering the sorted list is compared
with the existing elements and placed at its correct position.
So at the end all the elements from the unsorted list are sorted.
Takes O(n^2) time complexity and O(1) space

'''
def selectionSort(arr):
    print(arr)

arr = [3,1,-1,5,2]