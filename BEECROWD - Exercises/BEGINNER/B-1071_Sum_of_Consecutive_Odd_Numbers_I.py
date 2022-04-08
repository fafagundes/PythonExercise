"""
Read two integer values X and Y. Print the sum of all odd values between them.

Input
The input file contain two integer values.

Output
The program must print an integer number. This number is the sum off all odd values between both input values that must fit in an integer number.
"""

X = int(input())
Y = int(input())

soma = 0

if X == Y:
    print('0')
elif X < Y:
    Y -= 1
    for X in range(X, Y):
        X += 1
        if X % 2 != 0:
            soma += X

else:
    X -= 1
    for Y in range(Y, X):
        Y += 1
        if Y % 2 != 0:
            soma += Y
print(soma)