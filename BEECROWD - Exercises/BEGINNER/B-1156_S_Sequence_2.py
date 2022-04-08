"""
Write an algorithm to calculate and write the value of S, S being given by:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

Input
There is no input in this problem.

Output
The output contains a value corresponding to the value of S.
The value should be printed with two digits after the decimal point.
"""

S = 1 # Declaro a o valor de 1 para S conforme solicita
i = 2 # Aqui já declaro dois, pois a 1° div começa por ele

for c in range(3, 39, 2): # Começo do 3 e pulo de 2 em 2 para obter o 1° num
    S = S + (c/i) # Calculo 1 mais a divisão que solicita
    i += i # Aqui dodro o valor como solicita
print('{:.2f}'.format(S))

