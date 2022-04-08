"""
Read an integer N, which represents the number of following test cases. Each test case consists of three floating-point numbers, each one with one digit after the decimal point. Print the weighted average for each of these sets of three numbers, considering that the first number has weight 2, the second number has weight 3 and the third number has weight 5.

Input
The input file contains an integer number N in the first line. Each N following line is a test case with three float-point numbers, each one with one digit after the decimal point.

Output
For each test case, print the weighted average according with below example.
"""

N = int(input())

for c in range(0, N):
    W = list(map(float, input().split()))
    AV = (((W[0]*2) + (W[1]*3) + (W[2]*5)) / 10)
    print('{:.1f}'.format(AV))

