def sum(*args): 
    # args will be a tuple of all the values passed to sum 
    total = 0
    for item in args:
        total += item 
    return total


print(sum(342, 2, 7, 9,45,657,43,234,68,34,135))  # you can pass any number of arguments


