# Computing a compund interest : $1000 at 5% for 10 years using math.pow and formatting it with two decimals
# math.pow always returns a float

import math
p, r, t = 1000, 0.05, 10

amount = p * math.pow(1 + r, t)
print("After " + str(t) + " years: $" + f"{amount:,.2f}")
