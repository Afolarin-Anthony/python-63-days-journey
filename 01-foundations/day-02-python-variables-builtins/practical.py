# This code checks the type of each value with type().__name__
# It also compares a variable against a type with isinstance()

 
import builtins

name = "Anthony"
age = 32
height = 1.72
is_master = False
favorite = None

for var in (name, age, height, is_master, favorite):
    print(repr(var), "---->", type(var).__name__)

print(isinstance(age, int), isinstance(height, (int, float)))

a = [1, 2, 3]
b = a
b.append(4)
print(a)

print("Total builtin name:", len(dir(builtins)))
print([n for n in dir(builtins) if n.isupper()])
