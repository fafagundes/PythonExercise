"""
Write a program to read the coordinates (X, Y) of an indeterminate number of points in Cartesian system. For each point write the quadrant to which it belongs. The program finish when at least one of two coordinates is NULL (in this situation without writing any message).

Input
The input contains several tests cases. Each test case contains two integer numbers.

Output
For each test case, print the corresponding quadrant which these coordinates belong, as in the example.
"""

def quadrant():

    while True:
        x, y = list(map(int, input().split()))
        if x > 0 and y > 0:
            print(f"primeiro")
        elif x < 0 and y > 0:
            print(f"segundo")
        elif x < 0 and y < 0:
            print(f"terceiro")
        elif x > 0 and y < 0:
            print(f"quarto")
        elif x == 0 or y == 0:
            break


quadrant()


# X, Y = list(map(int, input().split()))
#
# while(True):
#     if X == 0 or Y == 0:
#         break
#     if X > 0 and Y > 0:
#         print('primeiro')
#     elif X < 0 and Y > 0:
#         print('segundo')
#     elif X < 0 and Y < 0:
#         print('terceiro')
#     elif X > 0 and Y < 0:
#         print('quarto')
#     X, Y = list(map(int, input().split()))
