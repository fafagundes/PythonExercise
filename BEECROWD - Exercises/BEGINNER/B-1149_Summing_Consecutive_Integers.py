"""
Write an algorithm to read a value A and a value N. Print the sum of N numbers from A (inclusive).
While N is negative or ZERO, a new N (only N) must be read. All input values are in the same line.

Input
The input contains only integer values, ​​can be positive or negative.

Output
The output contains only an integer value.

Input Sample
3 -1 0 -2 2

Output Sample
7
"""

X = list(map(int, input().split()))

A = X[0]
POS = int(len(X) - 1)
B = 0
N = 0

for posit in range(0, POS+1):
    B += X[posit]
    if posit > 0 and B > 0:
        N = B
    else:
        B = 0

SUM = A
for c in range(1, N):
    SUM = SUM + (A + c)
print(SUM)
