"""
Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to calculate the roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

Input
Read 3 floating-point numbers A, B and C.

Output
Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.
"""

A, B, C = list(map(float, input().split()))

DELTA = (B**2) - (4 * A * C)

if DELTA > 0 and A != 0:
    R1 = (-B + (DELTA**(1/2))) / (2 * A)
    R2 = (-B - (DELTA**(1/2))) / (2 * A)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
else:
    print(f"Impossivel calcular")
