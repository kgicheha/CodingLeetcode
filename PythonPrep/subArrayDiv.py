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
RESULT:
    return array of CONTIGIOUS segement that fits:
        the LENGTH of the segment matches bithday MONTH(m)
        SUM of the integers is equal to bithDAY (d)
'''
def birthday(s,d,m):
    print(s)


s = [2,2,1,3,2]
d = 4
m = 2

birthday(s,d,m)