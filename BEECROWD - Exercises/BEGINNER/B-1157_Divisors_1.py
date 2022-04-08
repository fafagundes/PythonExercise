"""Read an integer N and compute all its divisors.

Input
The input file contains an integer value.

Output
Write all positive divisors of N, one value per line.

Input Sample
6

Output Sample
1
2
3
6
"""

N = int(input())

for c in range(1, N+1):
    if N % 2 != 0:
        break
    else:
        if N % c == 0:
            print(c)
