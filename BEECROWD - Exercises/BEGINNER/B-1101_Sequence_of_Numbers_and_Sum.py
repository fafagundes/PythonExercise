"""
Read an undetermined number of pairs values M and N (stop when any of these values is less or equal to zero). For each pair, print the sequence from the smallest to the biggest (including both) and the sum of consecutive integers between them (including both).

Input
The input file contains pairs of integer values M and N. The last line of the file contains a number zero or negative, or both.

Output
For each pair of numbers, print the sequence from the smallest to the biggest and the sum of these values, as shown below.

2 3 4 5 Sum=14
3 4 5 6 Sum=18
"""

total = 0

M, N = list(map(int, input().split()))

while M > 0 or N > 0: # Aqui eu uso o while, mas eu não estudei a respeito

    if M == 0 or N == 0 or M < 0 or N < 0: # Condições para o programa parar ou seguir
        break
    elif M > N:
        A = N
        B = M
        for c in range(A, B+1): # Inverto se o primeiro número for maior para colocar no laço de repetição
            print('{} '.format(c), end="") # Inprimo ao lado os números conforme solicita no output
            total += c
        print('Sum={}'.format(total))
        total = 0
    else:
        for d in range(M, N+1):
            print('{} '.format(d), end="")
            total += d
        print('Sum={}'.format(total))
        total = 0

    M, N = list(map(int, input().split())) # Aqui solicito os dados novamente, pois estou dentro do laço
