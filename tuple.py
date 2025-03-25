# Create a tuple
example_tuple = (10, 20, 30, 40, 50)
print("Example tuple:", example_tuple)

# Access elements
print("First element:", example_tuple[0])
print("Last element:", example_tuple[-1])

# Slicing
print("Slice (index 1 to 3):", example_tuple[1:4])

# Tuple unpacking
a, b, c, d, e = example_tuple
print("Unpacked values:", a, b, c, d, e)

# Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)
print("Accessing an element in a nested tuple:", nested_tuple[1][0])

# Tuple methods
print("Count of 20 in tuple:", example_tuple.count(20))
print("Index of 30 in tuple:", example_tuple.index(30))

# Example use case: Returning multiple values from a function
def get_coordinates():
    return (10, 20, 30)

coordinates = get_coordinates()
print("Coordinates returned by function:", coordinates)