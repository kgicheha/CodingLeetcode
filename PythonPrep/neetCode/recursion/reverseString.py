def reverseString(s):

    if len(s) == 0:
        return s

    else:
        return reverseString(s[1::]) +  s[0]

    print("Reversed String: ", s)
s = "King"

print(reverseString(s))

'''
STEPS:
    BASE CASE:
    once you get to the begging of the string:
        return the string

    else:
        return call the function on the characters from the 1 index to the last index + first character

'''