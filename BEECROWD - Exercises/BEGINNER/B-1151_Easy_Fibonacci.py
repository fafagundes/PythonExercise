"""
The following sequence of numbers 0 1 1 2 3 5 8 13 21 ... is known as the Fibonacci Sequence. Thereafter, each number after the first 2 is equal to the sum of the previous two numbers.
Write an algorithm that reads an integer N (N < 46) and that print the first N numbers of this sequence.

Input
The input file contains an integer number N (0 < N < 46).

Output
The numbers ​​should be printed on the same line, separated by a blank space. There is no space after the last number.
"""

N = int(input())
t1 = 0 # São valores fixos
t2 = 1 # São valores fixos
c = 3 # Começo do 3 pois o 1 e 2 são fixos

print('{} {}'.format(t1, t2), end='') # Como são fixos(Não tem calculo) imprimo direto
while c <= N:
    t3 = t1 + t2 # Faço o calculo do t3 que é a soma dos anteriores
    print(' {}'.format(t3), end='')
    t1 = t2 # Aqui mudo somente o valor que será o próximo
    t2 = t3 # Mesmo caso aqui
    c += 1
print('') # Para o programa URI tem que ter uma linha vazia no final