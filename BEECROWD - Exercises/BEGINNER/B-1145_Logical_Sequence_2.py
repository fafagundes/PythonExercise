"""Write an program that reads two numbers X and Y (X < Y). After this, show a sequence of 1 to y, passing to the next line to each X numbers.

Input
The input contains two integer numbers X (1 < X < 20) and Y (X < Y < 100000).

Output
Each sequence must be printed in one line, with a blank space between each number, like the following example.

Input Sample
3 99

Output Sample
1 2 3
4 5 6
7 8 9
10 11 12
...
97 98 99
"""

def logical_sequence2():
    x, y = list(map(int, input().split()))
    for j in range(1, y + 1, x):
        num = ""
        for i in range(j, x+j):
            num = num + str(i) + " "
        print(num.rstrip())


logical_sequence2()


# def logical_sequence2():
#     x, y = list(map(int, input().split()))
#     for j in range(1, y + 1, x):
#         for i in range(j, x+j):
#             print(f"{i}", end=" ")
#         print()
#
#
# logical_sequence2()


# X, Y = list(map(int, input().split()))
# A = X
# saida = ''
#
# for c in range(1, Y+1):
#     if c < A: # Aqui vai imprimir com espaço no final
#         print(c, end=' ')
#     elif c == A: # Aqui tira o espaço no final e quebra a linha
#         print(c, end='')
#         print(saida)
#         A += X # Aqui vou acrescentando o contador de X em X




