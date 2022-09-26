"""
Write a program that reads an integer N. N * 2 lines must be printed by this program according to the example below. For numbers with more than 6 digits, all digits must be printed (no cientific notation allowed).

Input
The input file contains an integer N (1 < N < 1000).

Output
Print the output according to the given example.

Output Sample
1 1 1
1 2 2
2 4 8
2 5 9
3 9 27
3 10 28
4 16 64
4 17 65
5 25 125
5 26 126
"""

def logical_sequence(n):
    for i in range(1, n+1):
        print(f"{i} {i*i} {i*i*i}")
        print(f"{i} {i*i+1} {i*i*i+1}")


logical_sequence(6)

# def logical_sequence(n):
#     a = b = c = 1
#     print(f"{a} {b} {c}")
#     n = n*2
#     b = 2
#     c = 2
#     for i in range(n-1):
#         print(f"{a} {b} {c}")
#         if i % 2 == 0:
#             a += 1
#             b = a * a
#             c = a * b
#         if i % 2 != 0:
#             c = (a * b) + 1
#             b = (a * a) + 1
#
#
# logical_sequence(5)
#
# N = int(input())
#
# n1 = 1
# n2 = 1
# n3 = 1
#
# for c in range(0, N*2):
#     if c >= 2 and c % 2 == 0: # Na sequencia par, faz esses calculos
#         n1 += 1
#         n2 = n1 * n1
#         n3 = n1 * n2
#     elif c >= 1 and c % 2 != 0: # Como a sequencia é que depois(Sequencia ímpar) o segundo e terceiro número é eles mesmos + 1
#         n1 = n1
#         n2 += 1
#         n3 += 1
#     print('{} {} {}'.format(n1, n2, n3)) #Como a primeira condição não entra em nenhum dos requisitos acima
#     # vai imprimir 1 1 1.
