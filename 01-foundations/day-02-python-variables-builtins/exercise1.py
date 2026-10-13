# Day 2: Variables, Naming & Data types
# Module of the day: Builtins
# Exercise 1
# Create one variable for each core type, then print its type using type().__name__

text = "learning"
count = 63
pi = 3.14159
flag = True
nothing = None

# The loop

for v in (text, count, pi, flag, nothing):
    print(repr(v), "------>", type(v).__name__)
