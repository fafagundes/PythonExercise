"""
Read an integer N. This N will be the number of integer numbers X that will be read.

Print how many these numbers X are in the interval [10,20] and how many values are out of this interval.

Input
The first line of input is an integer N (N < 10000), that indicates the total number of test cases.
Each case is an integer number X (-107 < X < 107).
"""

def in_out(N):

    count_in = 0
    count_out = 0
    if N < 10000:
        for i in range(N):
            X = int(input())
            if 10 <= X <= 20:
                count_in += 1
            else:
                count_out += 1
        print(f"{count_in} in")
        print(f"{count_out} out")


in_out(int(input()))


# inv = 0
# out = 0
#
# N = int(input())
#
# for c in range(0, N):
#     X = int(input())
#     if X >= 10 and X <= 20:
#         inv += 1
#     else:
#         out += 1
#
# print('{} in'.format(inv))
# print('{} out'.format(out))

