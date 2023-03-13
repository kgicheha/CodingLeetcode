'''
1. Create BASE CASE
    if length of the given arry is less than or equal to 1:
        return the given array
    else:
        find the pivot --> use the last index in the array as the pivot


2. Initiliaze empty array to store the items that are greater than the pivot
3. Initialize empty array to store the items that are loqwe than the pivot

4. Iterate through array
    if the current item is > the pivot:
        store it into the item_greater array
    else:
        store the item into the items_lower array




'''

def quickSort(arr):
    length = len(arr)

    if length <= 1:
        return arr
    else:
        pivot = arr.pop()


    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quickSort(items_lower) + [pivot] + quickSort(items_greater)


arr = [3,2,6,7,1,2,4]
print(quickSort(arr))