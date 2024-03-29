"""
Read an undetermined number of pairs of integer values. Write a message for each pair indicating if this two numbers are in ascending or descending order.

Input
The input file contains several test cases. Each test case contains two integer numbers X and Y. The input will finished when X = Y.

Output
For each test case print “Crescente”, if the values X and Y are in ascending order, otherwise print “Decrescente”.
"""

def ascending_and_descending():

    while True:
        m, n = list(map(int, input().split()))

        if m != n:
            if m > n:
                print(f"Decrescente")
            else:
                print(f"Crescente")
        else:
            break


ascending_and_descending()


# X, Y = list(map(int, input().split()))
#
# while X != Y: # Se os números não forem iguais, fazer o loop
#     if X > Y:
#         print('Decrescente')
#     else:
#         print('Crescente')
#
#     X, Y = list(map(int, input().split()))

