"""
Read three point floating values (A, B and C) and verify if is possible to make a triangle with them. If it is possible, calculate the perimeter of the triangle and print the message:


Perimetro = XX.X


If it is not possible, calculate the area of the trapezium which basis A and B and C as height, and print the message:


Area = XX.X

Input
The input file has tree floating point numbers.

Output
Print the result with one digit after the decimal point.
"""
a, b, c = list(map(float, input().split()))

if a < (b+c) and b < (a+c) and c < (a+b):
    perimetro = a + b + c
    print('Perimetro = {:.1f}'.format(perimetro))
else:
    area = (((a + b) * c) / 2)
    print('Area = {:.1f}'.format(area))
