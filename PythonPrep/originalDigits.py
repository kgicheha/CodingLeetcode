from collections import Counter

'''
423. Reconstruct Original Digits from English

Given a string s containing an out-of-order English representation of digits 0-9,
return the digits in ascending order.

'''

'''
Example 1:

Input: s = "owoztneoer"
Output: "012"
'''

def originalDigits(s):
    c = Counter(s)
    n = [0]* 10

    n[0] =c['z']
    n[2] = c['w']
    n[4] = c['u']
    n[6] = c['x']
    n[8] = c['g']
    n[1] = c['o'] - n[0] - n[2] -n[4]
    n[3] = c['h'] - n[8]
    n[5] = c['f'] - n[4]
    n[7] = c['s'] - n[6]
    n[9] = c['i'] - n[5] - n[6] - n[8]

    output = []
    for i in range(10):
        output.append(str(i)* n[i])

    return "".join(output)
s = "owoztneoer"
print(originalDigits(s))