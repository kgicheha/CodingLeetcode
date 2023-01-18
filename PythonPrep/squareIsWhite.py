'''
1812. Determine Color of a Chessboard Square
You are given coordinates, a string that
represents the coordinates of a square of the chessboard.
Below is a chessboard for your reference.
eturn true if the square is white, and false if the square is black.
'''

'''
Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above,
the square with coordinates "a1" is black, so return false.
'''

'''
GIVEN:
    coordinates in a chessboard
STEPS:
    create a dictionary that separates the characters based on their index position
        characters that have even number index belong to even key
        characters that have odd number index belong to odd key

    if the the first character in the given coordinate is in even key in that dictionary:
        and the second character in the given coordinate is even
            return TRUE
        else return FALSE

    else (if the first character in the given coordinate is in the odd key in the dictionary)
        and the second character in the given coordinate is odd,
            return TRUE
        else:
            return FALSE
RESULT:
    return TRUE is the given coordinate is white,
    return FALSE if the given coordinate is black

'''

def squareIsWhite(coordinates):
    letters ={'even':['a', 'c','e', 'g'], 'odd':['b', 'd', 'f', 'h']}

    if coordinates[0] in letters['even']:
        if int(coordinates[1]) % 2 == 0:
            return True
        else:
            return False
    else:
        if int(coordinates[1]) % 2 != 0:
            return True
        else:
            return False


coordinates = "a1"
print(squareIsWhite(coordinates))