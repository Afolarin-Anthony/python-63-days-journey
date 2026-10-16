# PYTHON LEARNING
# DAY 3: Numbers and arithmetic
### DATE: 16th October 2026
### STATUS: In progress

## Concept: Owning every numeric operator, understand float pitfalls, and master the math module for real world calculations.
## The module that brings the concept to life is the math module

### Examples
- math.isclose(a,b) -----> the correct way to compare floats
- math.isqrt(n) -----> integer square root, no float error
- math.hypot(a,b) ----> distance without overflow
- math.tau() ----> The circle constant 2π.
- math.pow() -----> a fragile function for finding an exponential power.

 Any time I need powers and roots (sqrt, isqrt, exp, log), rounding (floor, ceil,
trunc), whole‑number math (factorial, gcd, lcm, comb), trigonometry (sin, cos, radians), or loat
safe comparison (isclose).

## What I learnt
- math.pow() always returns a float unlike "**".
- For math operations to be done and represented properly, use the math module, for complex ones, use the cmath module
- Arithmetic operations of floats (decimals) in python tend to give different results which is why isclose() is used to compare floats. This is regarded as more accurate.
-  

## More researched
- math.isnan(): Checks if a value is Not a Number (NaN). This occurs during invalid operations like 0 / 0 or subtracting infinity from infinity.
- math.isinf(): Checks if a value is positive or negative Infinity (inf or -inf). This happens when a number overflows Python's maximum floating-point limit or when dividing a non-zero number by zero.
- math.isfinite(): Checks if a value is a normal, valid number. It returns True if the number is neither NaN nor Infinity.**




