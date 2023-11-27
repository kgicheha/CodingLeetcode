def panagram(s):
    s = s.lower()

    seen = {}
    for char in s:
        if char not in seen:
            seen[char] = 1

        else:
            seen[char] += 1

    print(seen)