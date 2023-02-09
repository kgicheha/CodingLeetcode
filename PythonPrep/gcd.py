def euclid(a, b):
    remainder = 0

    while b > 0:
        remainder = a % b

        a = b
        b = remainder

    print(a)


euclid(30, 50)