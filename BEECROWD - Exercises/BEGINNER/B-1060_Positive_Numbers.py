"""
Write a program that reads 6 numbers. These numbers will only be positive or negative (disregard null values). Print the total number of positive numbers.

Input
Six numbers, positive and/or negative.

Output
Print a message with the total number of positive numbers.
"""

positivos = 0
i = 0

while i < 6: # Como ele começa a contar do 0, ele vai até 5
    a = float(input())
    if a > 0: # Verifico se o número é positivo
        positivos = positivos + 1 # Começo a contar o número positivo
    i = i + 1 # Aqui conto o i para chegar no 5 e parar de pedir mais que seis números
print("{} valores positivos".format(positivos))
