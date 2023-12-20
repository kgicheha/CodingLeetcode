def superDigit(n, k):
    # Write your code here
        def helper(n):
            total = 0

            for num in n:
                total += int(num)

            total = str(total)

            if len(total) == 1:
                return total
            else:
                return helper(total)

        p = str(helper(n) * k)
        return helper(p)

n = 9875
k = 4
print(superDigit(n, k))