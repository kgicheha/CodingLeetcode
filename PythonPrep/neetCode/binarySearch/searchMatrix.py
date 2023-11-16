def searchMatrix(matrix, target):

    if len(matrix) == 0:
        return False

    rows = len(matrix)
    columns = len(matrix[0])

    lp = 0
    rp = (rows * columns) - 1

    while lp <= rp:

        midPointIdx = (rp+ lp) // 2

        midPointRow = int(midPointIdx /columns)
        midPointColumn = int(midPointIdx % columns)
        midPointElement = matrix[midPointRow][midPointColumn]

        if midPointElement == target:
            return True
        elif midPointElement < target:
            lp += 1
        else:
            rp -= 1

    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
# Output: true
print(searchMatrix(matrix, target))

'''
Link: https://leetcode.com/problems/search-a-2d-matrix/

'''
'''
GIVEN:
    m * n matrix integer with:
        each row sorted in non-decreasing order
        the first integer of each row is > than the last integer of the previous role
    target integer

STEPS:
RESULT:
    if target in matrix:
        return True
    else:
        return False
'''