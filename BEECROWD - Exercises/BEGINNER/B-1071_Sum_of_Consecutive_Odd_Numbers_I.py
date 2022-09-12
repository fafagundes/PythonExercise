"""
Read two integer values X and Y. Print the sum of all odd values between them.

Input
The input file contain two integer values.

Output
The program must print an integer number. This number is the sum off all odd values between both input values that must fit in an integer number.
"""

def sum_odd_number():

    X = int(input())
    Y = int(input())

    sum_odd = 0
    if X > Y:
        X, Y = Y, X

    if X == Y:
        print(f"0")
    else:
        for X in range(X+1, Y):

            if X % 2 != 0:
                sum_odd += X
        print(f"{sum_odd}")


sum_odd_number()




# X = int(input())
# Y = int(input())
#
# soma = 0
#
# if X == Y:
#     print('0')
# elif X < Y:
#     Y -= 1
#     for X in range(X, Y):
#         X += 1
#         if X % 2 != 0:
#             soma += X
#
# else:
#     X -= 1
#     for Y in range(Y, X):
#         Y += 1
#         print(f"Y: {Y}")
#         if Y % 2 != 0:
#             soma += Y
#             print(f"soma: {soma}")
#
# print(soma)
