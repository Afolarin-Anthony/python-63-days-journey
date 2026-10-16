# To find all Pythagorean triples (a, b, c) with c <= 30 using math.hypot and math isclose.
# math.hypot returns a float, so comparing it to the integer c with isclose is the safest habit

import math
triples = []
for c in range(1, 31):  # Sets the hypotenuse c. The range generates numbers from 1 to 30.
    for b in range(1, c): # Sets the second leg b. Because it stops at c, it guarantees that b is always smaller
        for a in range(1, b + 1): # • Sets the shortest leg a. Because it stops at b + 1, it guarantees that a is less than or equal to b
            if math.isclose(math.hypot(a, b), c):
                triples.append((a,b,c))
print(triples)
