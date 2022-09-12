"""
Read an integer value X and print the 6 consecutive odd numbers from X, a value per line, including X if it is the case.

Input
The input will be a positive integer value.

Output
The output will be a sequence of six odd numbers.
"""

def odd_number():

    X = int(input())
    v_count = 0
    while v_count < 6:

        if X % 2 != 0:
            print(f"{X}")
            v_count += 1
            X += 1
        else:
            X += 1


odd_number()

# X = int(input())
#
# i = 0
#
# while i < 6:
#     if (X % 2) != 0:
#         print('{}'.format(X))
#         X += 1
#     else: # Como precisamos de 6 números impares e o contador vai até seis, nesse "else" eu peço para ignorar os pares
#         X += 1
#         i -= 1
#     i = i + 1