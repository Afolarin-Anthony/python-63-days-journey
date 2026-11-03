# Slicing a list in python

numbers = [10, 20, 30, 40, 50]

print("List 1")
print(numbers[1:4])
print("\n")
print("List 2")
print(numbers[:3])
print("\n")
print("List 3")
print(numbers[2:])
print("\n")
print("List 4")
print(numbers[::-1])
print("\n")


# Nested Lists (Lists contain other lists)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Accessing nested elements

print(matrix[1][2]) # The first index gives the postion of the first layer of lists. Then the second index gives the postion of an element in the first list selected
