'''
Given n names and phone numbers,
assemble a phone book that maps friends' names to their
respective phone numbers.
You will then be given an unknown number of names
to query your phone book for.
For each name queried,
print the associated entry from your phone book
on a new line in the form name=phoneNumber;
 if an entry for name is not found, print Not found instead.

'''

'''

'''


n = int(input())
phonebook = {}

for i in range(n):
    line = input()
    pair = line.split()
    phonebook[pair[0]] = pair[1]


while True:
    try:
        name = input()
    except EOFError as e:
        break
    if name not in phonebook.keys():
        print("Not found")
    else:
        print(f"{name}={phonebook[name]}")
