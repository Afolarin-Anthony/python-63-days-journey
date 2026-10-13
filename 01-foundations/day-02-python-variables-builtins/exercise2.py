# Day 2: Variables, Naming & Data types
# Module of the day: Builtins
# Exercise 2
# Writing a mini-type checker that correctly identifies True as bool )and explains that bool is an int subclass)

value = True
if isinstance(value, bool):
    print("bool -- also an int subclass:", issubclass(bool, int))
elif isinstance(value, int):
    print("int")
else:
    print(type(value).__name__)
