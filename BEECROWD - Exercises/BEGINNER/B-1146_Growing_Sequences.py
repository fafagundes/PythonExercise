"""
Your program must read an integer X indefinited times (the program must stop when X is equal to zero). For each X print the sequence from 1 to X, with one space between each one of these numbers.

PS: Be carefull. Don't leave any space after the last number of each line, otherwise you'll get Presentation Error.

Input
The input file contains many integer numbers. The last one is zero.

Output
For each number N of the input file, one output line must be printed, from 1 to N like the following example. Be careful with blank spaces after the last line number.

Input Sample
5
10
3
0

Output Sample
1 2 3 4 5
1 2 3 4 5 6 7 8 9 10
1 2 3
"""

def growing_sequences(x):
    num = ""
    for i in range(1, x+1):
        num = num + str(i) + " "
    return num.rstrip()


x = 1
while True:
    x = int(input())
    if x != 0:
        print(growing_sequences(x))
    else:
        break


# X = 1
#
# while X != 0:
#     X = int(input())
#     for c in range(1, X+1):
#         if c < X:
#             print(c, end=' ')
#         elif c == X:
#             print(c, end='\n')


