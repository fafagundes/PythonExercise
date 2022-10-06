"""
The program must read an integer X indefinite times (stop when X=0). For each X, print the sum of five consecutive even
numbers from X, including it if X is even. If the input number is 4, for example, the output must be 40,
that is the result of the operation: 4+6+8+10+12. If the input number is 11, for example, the output must be 80,
that is the result of 12+14+16+18+20.

Input
The input file contains many integer numbers. The last one is zero.

Output
Print the output according to the example below.
"""

def sum_even():

    while True:
        x = int(input())
        if x == 0:
            break
        else:
            if x % 2 != 0:
                x += 1

            result = 0
            for i in range(5):
                result += x
                x += 2

            print(result)


sum_even()


# while True:
#     X = int(input())
#     if X == 0:
#         break
#     if X % 2 != 0:
#         X += 1
#     total = 0
#     a = 1
#     while a <= 5:
#         total += X
#         a += 1
#         X += 2
#     print(total)

