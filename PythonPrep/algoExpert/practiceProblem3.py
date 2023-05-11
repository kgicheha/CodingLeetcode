'''
GIVEN:
    m by n 2d binary grid called grid --> represents a map of "1" and "0" string
        1s represent land
        0s reps water

STEPS:
    2D ARRAY:
        [1][0]

    traverse given 2D array:
        if the current value is "1":
            check to see what the value to the left, right, above, and below are:
                if value of the left is "0"


RESULT:
    return the number of islands
        islands is defined by adjacent lands(next to each other) that are connected either vertically or horizontally
        can asssume that all edges are surrounded by water
'''

'''
EXAMPLE 1:
    Input: grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    Output: 1

EXAMPLE 2:
Input: grid = [
        ["0","1","0"],
        ["0","1","0"],
        ["0","0","0"],
    ]
    Output = 2

Example 3:
Input: grid = [
        ["1","0"],
        ["1","0"],
        ["1","1"],
    ]
    Output  = 1


Example 4:
Input: grid = [
        ["1","0"],
        ["0","0"],
        ["0","0"],
    ]
    Output = 1
'''

def isIsland(grid):

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                checkisIslandHelper(i, j, grid)
                count += 1

    return count

def checkisIslandHelper(i, j, grid):
    if (i < 0) or (i >= len)(grid) or (j < 0) or (j >= len(grid[i])) or grid[i][j] == "0":
        return

    grid[i][j] == "0"

    checkisIslandHelper(i - 1, j) #left
    checkisIslandHelper(i + j, j) #right
    checkisIslandHelper(i, j + 1) #up
    checkisIslandHelper(i, j - 1) #down

grid = [
        ["1","0"],
        ["0","0"],
        ["0","0"],
    ]

print(isIsland(grid))