"""
Make a program that prints the sequence like the following exemple.

Input
This problem doesn't have input.

Output
Print the sequence like the example below.

I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=7
I=3 J=6
I=3 J=5
...
I=9 J=7
I=9 J=6
I=9 J=5
"""

for c in range(1, 10, 2):
    print('I={} J={}'.format(c, 7))
    print('I={} J={}'.format(c, 6))
    print('I={} J={}'.format(c, 5))
