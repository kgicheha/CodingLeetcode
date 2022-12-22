'''
Find the maximum(largest) value in a finite sequence of integers

'''

def max_value(arr):
    #BRUTE FORCE
    # max_num = arr[0]

    # for i in arr:
    #     if(max_num < i):
    #         max_num = i

    # print(max_num)

    #OPTIMAL
    max_num = max(arr)
    print(max_num)

max_value([2,3,1,5,4])
