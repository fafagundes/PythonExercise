"""
Write a program that reads two integer numbers X and Y and calculate the sum of all number not divisible by 13 between them, including both.

Input
The input file contains 2 integer numbers X and Y without any order.

Output
Print the sum of all numbers between X and Y not divisible by 13, including them if it is the case.
"""

divR = A = B = 0

X = int(input())
Y = int(input())

if Y < X:
    A = Y
    B = X
else:
    A = X
    B = Y

for A in range(A, B+1):
    if A % 13 != 0:
        divR += A
    A += 1
print(divR)

