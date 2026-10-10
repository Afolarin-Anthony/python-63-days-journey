#  Write a script that prints how many command‑line arguments it received and exits with
code 0.

import sys # importing the sys module
print("Number of arguments: ", len(sys.argv)) # Count the number of arguments
sys.exit(0) # meaning success
