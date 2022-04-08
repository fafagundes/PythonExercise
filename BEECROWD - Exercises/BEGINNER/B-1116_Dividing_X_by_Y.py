"""
Write a program that read two numbers X and Y and print the result of dividing the X by Y. If it's not possible, print the message "divisao impossivel".

Input
The input contains an integer number N. This N is the quantity of pairs of integer numbers X and Y read (dividend and divisor).

Output
For each test case print the result of this division with one digit after the decimal point, or “divisao impossivel” if it isn't possible to perform the calculation.

Obs.: Be carefull. The division between two integers in some languages generates another integer. Use cast:)
"""

N = int(input())

for c in range(0, N):
    X, Y = list(map(int, input().split()))
    if Y == 0:
        print('divisao impossivel')
    else:
        div = X / Y
        print(div)
