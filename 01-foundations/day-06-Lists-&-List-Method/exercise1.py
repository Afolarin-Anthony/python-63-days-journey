# Creating a list of Foodstuffs.

foodstuffs = ["Garri", "Rice", "Beans", "Yam", "Palm Oil", "Salt", "Pepper"]
print(foodstuffs) # Printing it out the list.

# Indexing a list
# For the foodstuffs variable.
print(foodstuffs[0])
print(foodstuffs[-2])

# Altering a value in a List
foodstuffs[3] = "Potato" # Replacing Yam with Potato.
print(foodstuffs) # Confirming the alteration.

# Appending adds an item to the end of the list (n - 1).
foodstuffs.append("Onions") # Added onions to the list.
print(foodstuffs)

# If you were to insert a value at a specific index, you use the insert() method
foodstuffs.insert(3, "Ginger") # Added Ginger to the 3 index.

# Adding multiple values at once, you use extend() method.
foodstuffs.extend(["Yam", "Garlic"])
print("Added yam and garlic with extend" foodstuffs)

# Removing values from a list.
# Removing by name or value.
foodstuffs.remove("Garlic") # I don't eat garlic.

print(foodstuffs)

# Removing by index
removed_item = foodstuffs.pop(4) # I wonder what is at index 4, let find it out.

# We can check what was removed.
print(removed_item)

# Ways we can find and also manipulate them.
# Assuming we already know what is in the list.
print(foodstuffs.index("Rice"))


# Counting the number of occurrences i.e sequence in a list).
# We use the count() method.
numbs = [4,6,8,8,1,3,5,9,8,8,0,2]
print(numbs.count(8)) # Counting how many 8 we have in the List.

# We can use sort() to arrange in ascending order.
numbs.sort()
print(numbs)

# Arranging in descending order.
numbs.sort(reverse=True)

# Take note that reversing is different from sorting.
# Also sorting, reversal can be sorted.
print(foodstuffs.sort())
print(numbs.reverse())

# If we were to clear the list 
numbs.clear()
print(numbs)


# Copying of sets
a = [1,2,3]
b = a.copy()
b.append(4)
print(a) # Separate from b
print(b) # Separate from a
