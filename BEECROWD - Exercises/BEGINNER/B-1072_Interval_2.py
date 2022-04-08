"""
Read an integer N. This N will be the number of integer numbers X that will be read.

Print how many these numbers X are in the interval [10,20] and how many values are out of this interval.

Input
The first line of input is an integer N (N < 10000), that indicates the total number of test cases.
Each case is an integer number X (-107 < X < 107).
"""

inv = 0
out = 0

N = int(input())

for c in range(0, N):
    X = int(input())
    if X >= 10 and X <= 20:
        inv += 1
    else:
        out += 1

print('{} in'.format(inv))
print('{} out'.format(out))

