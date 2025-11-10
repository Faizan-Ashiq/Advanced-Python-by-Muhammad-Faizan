numbers = [1, 2, 3, 45, 4, 21,345,56,3437,787,435534]

# def square(x):
#     return x * x 


new = list(map(lambda x: x*x, numbers))
# new = list(map(square, numbers))
print(new)