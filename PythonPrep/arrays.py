'''
Given an array, A , of N integers,
print A's elements in reverse order as a single line of space-separated numbers.

Example
4
1 2 3 4

print [4 3 2 1]

'''

def rev_array(arr):

    #BRUTE FORCE
    for i in arr[::-1]:
        print(i, end=" ")


    #ONE LINER
    print(*reversed(arr))



rev_array([1,2,3,4])