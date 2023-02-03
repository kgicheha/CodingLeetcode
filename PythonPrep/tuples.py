def tuples():
    tuple_length = int(input())
    raw_input = input().split(" ")
    tuple_converter = tuple(map(int, raw_input))
    print(hash(tuple_converter))