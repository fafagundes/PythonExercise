"""
Make a program that prints the sequence like the following exemple.

Input
This problem doesn't have input.

Output
Print the sequence like the example below.

I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
...
I=9 J=15
I=9 J=14
I=9 J=13
"""

def sequence_IJ_3():

    j_start = 7
    j_end = 4
    for i in range(1, 10, 2):
        for j in range(j_start, j_end, -1):
            print(f"I={i} J={j}")
        j_start += 2
        j_end += 2


sequence_IJ_3()


# X1 = 7
# X2 = 6
# X3 = 5
# for c in range(1, 10, 2):
#     print('I={} J={}'.format(c, X1))
#     print('I={} J={}'.format(c, X2))
#     print('I={} J={}'.format(c, X3))
#     X1 += 2
#     X2 += 2
#     X3 += 2