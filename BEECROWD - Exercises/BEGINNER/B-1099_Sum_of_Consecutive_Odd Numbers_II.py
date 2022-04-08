"""
Read an integer N that is the number of test cases. Each test case is a line containing two integer numbers X and Y. Print the sum of all odd values between them, not including X and Y.

Input
The first line of input is an integer N that is the number of test cases that follow. Each test case is a line containing two integer X and Y.

Output
Print the sum of all odd numbers between X and Y.
"""

N = int(input())

sumone = 0
sumtwo = 0

for c in range(0, N):
    X, Y = list(map(int, input().split()))

    if X > Y:
        A = Y
        B = X
        #print(A, B)
        for i in range(A+1, B):
            if A == B:
                sumone = 0
            elif i % 2 != 0:
                sumone += i
        print(sumone) # Espero o laço de repetição terminar para imprimir
        sumone = 0 # Zero o contado para o outro laço posterior
    else:
        for j in range(X+1, Y):
            if X == Y:
                sumtwo = 0
            elif j % 2 != 0:
                sumtwo += j
        print(sumtwo)
        sumtwo = 0
