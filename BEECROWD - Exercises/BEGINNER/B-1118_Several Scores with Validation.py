"""
Write an program to read two scores of a student. Calculate and print the semester average. The program must accept only valid scores (a score must fit in the range [0.10]). Each score must be validated separately.

The program must print a message "novo cálculo (1-sim 2-nao)" that means "new calculate (1-yes 2-no)". After, the input will be (1 or 2). 1 means a new calculation, 2 means that the execution must be finished.

Input
The input file contains several positive or negative floating-point (double) values​. After the input of 2 valid scores, an integer number X will be read. Your program must stop when X = 2.

Output
If an invalid score is read, must be printed the message "nota inválida". When two valid scores are read, the message "media = " must be printed folowed by the average between these 2 scores. The message "novo cálculo (1-sim 2-nao)" must be printed after reading X. This message should be displayed again if the standard input number for X is less than 1 or greater than 2, as example below.

The output average must be printed with 2 digits after the decimal point.
"""

# Declaração das variaveis
soma = 0
c = 0
X = 0

a = float(input()) # Solicito informações

while(True): # Enquanto solicitar informações e não houver um break
    if a >= 0 and a <= 10: # Se o número está entre 0 e 10
        soma += a # Pego o número e adiciono na soma
        c += 1 # faço um contador
        if c == 2: # se o contador recebeu dois números
            media = soma / 2 # Calculo a média
            print('media = {:.2f}'.format(media)) # Imprimo a média
            X = int(input('novo calculo (1-sim 2-nao)\n')) # Peço informações se quer continuar
            a = 0 # Zero as variaveis, pois o calculo foi feito e se querer continuar devem estar zeradas
            c = 0
            soma = 0
            while 1 != X != 2: # Aqui faço um outro "enquanto" caso não for digitado 1 ou 2
                X = int(input('novo calculo (1-sim 2-nao)\n'))
            if X == 1: # Se for 1, digo novamente que a varialvel vai ficar zerada, pois vai solicitar a informação no final
                a = 0
            elif X == 2: # aqui paro o programa
                break

    else:
        print('nota invalida') # Aqui é a condição contraria a primeira do 0 a 10
    a = float(input()) # Peço a informação novamente para continuar o enquanto
