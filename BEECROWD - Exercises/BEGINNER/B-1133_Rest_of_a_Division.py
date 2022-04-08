"""
Write a program that reads two integer numbers X and Y. Print all numbers between X and Y which dividing it by 5 the rest is equal to 2 or equal to 3.

Input
The input file contains 2 any positive integers, not necessarily in ascending order.

Output
Print all numbers according to above description, always in ascending order.
"""

X = int(input())
Y = int(input())

if Y < X:
    A = Y
    B = X
else:
    A = X
    B = Y

for A in range(A+1, B):
    if A % 5 == 2 or A % 5 == 3:
        print(A)
    A += 1
