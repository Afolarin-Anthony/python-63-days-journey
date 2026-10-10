# printing my Python version as a string, then printing the first three paths Python searches for modules(sys.path)

import sys
print(sys.version) # prints the version
for path in sys.path[:3] # A for loop printing the first three path pythons uses to search for imports
  print(path)
