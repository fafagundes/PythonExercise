"""
Make a program that prints the sequence like the following example.

Input
This problem doesn't have input.

Output
Print the sequence like the example below.

I=1 J=60
I=4 J=55
I=7 J=50
...
I=? J=0
"""

def sequence_IJ_1():

    i = 1
    for j in range(60, -1, -5):
        print(f"I={i} J={j}")
        i += 3


sequence_IJ_1()

# I = 1
#
# for c in range(60, -1, -5):
#     print('I={} J={}'.format(I, c))
#     I += 3


