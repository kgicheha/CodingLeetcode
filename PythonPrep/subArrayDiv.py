'''
Two children, Lily and Ron, want to share a chocolate bar.
Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

    The length of the segment matches Ron's birth month, and,
    The sum of the integers on the squares is equal to his birth day.

Determine how many ways she can divide the chocolate.
'''

'''
Example
s = [2,2,1,3,2]
d = 4
m = 2

Lily wants to find segments summing to Ron's birth day, d = 4
with a length equalling his birth month, m = 2.
In this case, there are two segments meeting his criteria: [2,2] and [1,3]
'''

'''
GIVEN:
    s: represents an array
    d: represents day of his birthday
    m: represents month of his birthday
STEPS:
    inialize left pointer equal to 0
    initialize right pointers equal to m
        difference between left pointer and M represents the size of the window

    initialize total segment count to 0
        this will keep count of the subarray that meet the criteria

    While right pointer is less than or equal to the length of array:

       get the sum of the sub elements from the left pointer and the right pointer

        if(sum == d) :
            increment total segment count by 1

        increment left pointer by 1
        increment right pointer by 1

    return the total segment count

'''
def birthday(s,d,m):

    left = 0
    right = m

    total_seg_count = 0

    while right <= len(s):

        sumSubArry = sum(s[left: right])

        if sumSubArry == d:
            total_seg_count += 1

        left += 1
        right +=1


    print(total_seg_count)

s = [2,2,1,3,2]
d = 4
m = 2

birthday(s,d,m)