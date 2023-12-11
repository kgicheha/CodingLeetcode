def superDigit(n, k):
    # Write your code here

    stringVersion = str(n)

    result = [0]

    for i in range(n):
        for char in stringVersion:
            helperFunction(char, result)

    return result

def helperFunction(char, result):
    intVersion = int(char)

    result[0] += intVersion

superDigit(n, k)