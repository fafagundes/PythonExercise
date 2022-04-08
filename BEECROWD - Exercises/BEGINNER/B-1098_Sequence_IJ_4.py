"""
Make a program that prints the sequence like the following example.

Input
This problem doesn't have input.

Output
Print the sequence like the example below.

I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?
"""

# Estrtura de repetição com condições aninhadas

#-- Declarando as variaveis --#
X1 = 1
X2 = 2
X3 = 3
I = 0

#--Estrtura de repericação que conta até 20 pulando de 2 em 2
for c in range(0, 21, 2):
    if c == 0: # Verifica o primeiro laço e já imprime os resultados iniciais
        print('I={} J={}'.format(I, X1))
        print('I={} J={}'.format(I, X2))
        print('I={} J={}'.format(I, X3))
    elif c > 0 and c <= 19: # Verifica até o penultimo laço e faz um contador
        X1 += 0.2
        X2 += 0.2
        X3 += 0.2
        I += 0.2
        if I == 1.0 or X1 == 2.0 or X2 == 3.0 or X3 == 4.0: # Tira casas decimais para quando for n.0
            print('I={:.0f} J={:.0f}'.format(I, X1))
            print('I={:.0f} J={:.0f}'.format(I, X2))
            print('I={:.0f} J={:.0f}'.format(I, X3))
        else:                                               # Quando não for imprime com uma casa decimal
            print('I={:.1f} J={:.1f}'.format(I, X1))
            print('I={:.1f} J={:.1f}'.format(I, X2))
            print('I={:.1f} J={:.1f}'.format(I, X3))


    else: # Ajusta resultado final
        X1 += 0.2
        X2 += 0.2
        X3 += 0.2
        print('I={:.0f} J={:.0f}'.format(I, X1))
        print('I={:.0f} J={:.0f}'.format(I, X2))
        print('I={:.0f} J={:.0f}'.format(I, X3))
