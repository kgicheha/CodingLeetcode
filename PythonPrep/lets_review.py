'''
Given a string, S , of length N  that is indexed from 0 to N-1 ,
print its even-indexed and odd-indexed characters as 2 space-separated
strings on a single line (see the Sample below for more detail).

Example

s = adbecf
Print abc def
'''


def lets_review(s):
    n = int(s())
    for _ in range(n):
        string = s()
        print(string[::2], string[1::2])



lets_review("adbecf")