# A python script that expects arguments but gracefully exits if there are none.

import sys

print("This Afolarin Anthony using python", sys.version_info, "running on", sys.platform)
print("The name of the script is:", sys.argv[0])
print("The arguments added to it are:", sys.argv[1:])

# Now looping
for i, arg in enumerate(sys.argv):
    print(f"argv[{i}] = {arg!r}")

# Control flow
if len(sys.argv) < 2:  # if arguments are less than two
    print("Usage: Python Day_1 challenge", file=sys.stderr)
    sys.exit(1) # give the error gracefully

print("Hello,", sys.argv[1],"!")
