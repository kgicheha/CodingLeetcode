def isUnique(num1, num2):
    uniqueCounter = [0]

    while num1 <= num2:
        num1 = str(num1)
        uniqueChecker(num1, uniqueCounter)

        num1 = int(num1)
        num1 += 1

    return uniqueCounter[0]

def uniqueChecker(num, uniqueCounter):
    seen = set()
    for i in range(len(num)):

        if num[i] not in seen:
            seen.add(num[i])
        else:
            return
    if len(seen) == len(num):
        uniqueCounter[0] += 1



print(isUnique(1,100))