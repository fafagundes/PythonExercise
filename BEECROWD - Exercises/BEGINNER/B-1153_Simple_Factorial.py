"""
Read a value N. Calculate and write its corresponding factorial. Factorial of N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Input
The input contains an integer value N (0 < N < 13).

Output
The output contains an integer value corresponding to the factorial of N.
"""

N = int(input())

f = 1
c = N
resul = N

for x in range(N-1, 0, -1):
    resul = resul * x
print(resul)


"""
while c > 0: # Como o último resultado tem que ser 1 ou maior...
    print('{}'.format(c), end='') # Imprime todos os contadores para ficar bonito e junta
    print(' x ' if c > 1 else ' = ', end='') # Aqui ele colocamos um if dentro do print para deixar mais visual o resultado
    f *= c # primeiro faz 5 x 1
    c -= 1 # Aqui fica 4, depois 3, 2, 1...
print('{}'.format(f))
"""