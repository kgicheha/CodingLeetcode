'''
821. Shortest Distance to a Character

Given a string s and a character c that occurs in s,
return an array of integers answer where answer.length == s.length
and answer[i] is the distance from index i to the closest occurrence
of character c in s.

The distance between two indices i and j is abs(i - j),
where abs is the absolute value function.


EXAMPLE:
Input: s = "aaab", c = "b"
Output: [3,2,1,0]
'''

'''
GIVEN:
    string
    character
STEPS:
RESULTS:

'''
def shortestToChar(s, c):

    left = 0
    right = len(s) - 1
    distance = 0
    output = []

    print(right)

    while left <= right:
        distance = right - left
        if s[left] == c:
            output.append(distance)
            right -= 1
        elif s[right] == c:
            output.append(distance)
            left += 1

    print(output)


s = "abaa"
c = "b"
shortestToChar(s, c)
