"""
Read an integer value X (1 <= X <= 1000).  Then print the odd numbers from 1 to X, each one in a line, including X if is the case.

Input
The input will be an integer value.

Output
Print all odd values between 1 and X, including X if is the case.
"""

X = int(input())

i = 1

if 1 <= X <= 1000:
    while i <= X:
        if (i % 2) != 0:
            print('{}'.format(i))
        i = i + 1


