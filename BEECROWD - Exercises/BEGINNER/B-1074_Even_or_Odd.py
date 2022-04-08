"""
Read an integer value N. After, read these N values and print a message for each value saying if this value is odd, even, positive or negative. In case of zero (0), although the correct description would be "EVEN NULL", because by definition zero is even, your program must print only "NULL", without quotes.

Input
The first line of input is an integer N (N < 10000), that indicates the total number of test cases. Each case is a integer number X (-107 < X <107)..

Output
For each test case, print a corresponding message, according to the below example. All messages must be printed in uppercase letters and always will have one space between two words in the same line.
"""

N = int(input())

result = ''
X = 0

for c in range(0, N):
    X = int(input())

    if X == 0:
        result = 'NULL'
    elif X > 0 and X % 2 == 0:
        result = 'EVEN POSITIVE'
    elif X < 0 and X % 2 == 0:
        result = 'EVEN NEGATIVE'
    elif X > 0 and X % 2 != 0:
        result = 'ODD POSITIVE'
    else:
        result = 'ODD NEGATIVE'

    print(result)

