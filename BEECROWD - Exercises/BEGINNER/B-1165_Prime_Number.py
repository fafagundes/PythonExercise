"""
A Prime Number is a number that is divisible only by 1 (one) and by itself.
For example the number 7 is Prime, because it can be divided only by 1 and by 7.

Input
The input contains several test cases. The first contains the number of test cases N (1 ≤ N ≤ 100).
Each one of the following N lines contains an integer X (1 < X ≤ 107), that can be or not a prime number.

Output
For each test case print the message “X eh primo” (X is prime) or “X nao eh primo” (X isn't prime)
according with to above specification.
"""

def prime_number(n):
    for i in range(n):
        x = int(input())
        count = 0
        for j in range(1, x+1):
            if x % j == 0:
                count += 1
        if count == 2:
            print(f"{x} eh primo")
        else:
            print(f"{x} nao eh primo")


prime_number(int(input()))


# N = int(input())
#
# for c in range(0, N):
#     X = int(input())
#     total = 0
#     for a in range(1, X+1):
#         if X % a == 0:
#             total += 1
#     if total == 2:
#         print('{} eh primo'.format(X))
#     else:
#         print('{} nao eh primo'.format(X))
