'''
Without using any string methods, try to print the following:

1,2,3,...n

'''

def print_string(n):

    for i in range(1, n+1):
        print(i, end='')

print_string(5)