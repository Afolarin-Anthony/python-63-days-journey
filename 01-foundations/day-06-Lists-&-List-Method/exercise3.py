# Looping through lists
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)


# Using enumerate()
# This is vital if we are to loop through position and value

for index, fruit in enumerate(fruits):
    print(index, fruit)


# If you want to start from a specific numbering

for index, fruits in enumerate(fruits, start=1):
    print(index, fruit) # Counts it starting with 1 not 0
