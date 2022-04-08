"""
Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to calculate the roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

Input
Read 3 floating-point numbers A, B and C.

Output
Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.
"""

from math import sqrt
a, b, c = map(float, input().split())

x = (b**2)-(4*a*c)

if a == 0:
    print('Impossivel calcular')
elif x > 0:
    x = x**(1/2)
    x1 = (-b + x) / (2 * a)
    print("R1 = {:.5f}".format(x1))
    x2 = (-b - x) / (2 * a)
    print("R2 = {:.5f}".format(x2))

else:
    print('Impossivel calcular')
