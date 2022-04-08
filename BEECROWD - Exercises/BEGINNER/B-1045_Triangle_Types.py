"""
Read 3 double numbers (A, B and C) representing the sides of a triangle and arrange them in decreasing order, so that the side A is the biggest of the three sides. Next, determine the type of triangle that they can make, based on the following cases always writing an appropriate message:
if A ≥ B + C, write the message: NAO FORMA TRIANGULO
if A2 = B2 + C2, write the message: TRIANGULO RETANGULO
if A2 > B2 + C2, write the message: TRIANGULO OBTUSANGULO
if A2 < B2 + C2, write the message: TRIANGULO ACUTANGULO
if the three sides are the same size, write the message: TRIANGULO EQUILATERO
if only two sides are the same and the third one is different, write the message: TRIANGULO ISOSCELES
Input
The input contains three double numbers, A (0 < A) , B (0 < B) and C (0 < C).

Output
Print all the classifications of the triangle presented in the input.
"""

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

maior_AB = (A + B + abs(A - B))/2

maior = (maior_AB + C + abs(maior_AB - C))/2

if maior == B:
    B = A
    A = maior
if maior == C:
    C = A
    A = maior

if A >= B + C: #Não precisa dos parenteses, não em Python
  print("NAO FORMA TRIANGULO")
else:
  if (A**2) == ((B**2)+(C**2)):
    print("TRIANGULO RETANGULO")
  elif (A**2) > ((B**2)+(C**2)):
    print("TRIANGULO OBTUSANGULO")
  elif (A**2) < ((B**2)+(C**2)):
    print("TRIANGULO ACUTANGULO")
  if (A == B) and (B == C) and (C == A): #Aqui você poderia ter colocado A == B == C em Python esse tipo de comparação é válida, diferente de C, como você está aplicando
    print("TRIANGULO EQUILATERO")
  elif (A == B) or (B == C) or (C == A): #Mesma coisa, pode remover os parênteses
    print("TRIANGULO ISOSCELES")
