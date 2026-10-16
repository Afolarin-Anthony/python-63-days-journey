import math

print("14/5 = ", 14 / 2, "14 // 5 = ", 14 // 5, "14 % 5 = ", 14 % 5)
print("4**10 = ", 4 ** 10, "issqrt(225) = ", math.isqrt(225))
print("Factorial(5) =", math.factorial(5))

print("pi = ", round(math.pi, 4),"e = ", round(math.e, 4))

for r in range (1, 6):
    area = math.pi * r ** 2
    print(f"circle r ={r}: area={area:8.2f}")

print("gcd(48, 18) =", math.gcd(48,18), " lcm(4,6) = ", math.lcm(4, 6))
print("hypot(3,4) =", math.hypot(3,4))

a, b = 0.1 + 0.2, 0.3
print("a == b?", a == b)
print("isclose?", math.isclose(a, b))
