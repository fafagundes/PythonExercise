"""
Write a program that reads two integers: X and Z (Z must be read as many times as necessary, until a number greater than X is read). Count how many integers must be summed in sequence (from and including X) so that the sum exceeds Z the minimum possible and write this number.

The input may have, for example, the numbers ​​21 21 15 30. In this case, the number 21 is assumed for X, The numbers 21 and 15 must be ignored because they are smaller or equal to X. The number 30 is within the specification (greater than X) and is valid. So, the final result must be 2 for this test case, because the sum (21 + 22) is bigger than 30.

Input
The input contains only integer values​​, one per line, which may be positive or negative. The first number is the value of X. The next line will contain Z. If Z does not meet the specification of the problem, it should be read again, as many times as necessary.

Output
Print a line with an integer number representing the among of integer numbers that must be summed.
"""

def exceeding_z():
    x = int(input())
    z = total = count = 0

    while z <= x:
        z = int(input())
        if z > x:
            for i in range(x, z):
                total += i
                count += 1
                if total > z:
                    print(count)
                    break


exceeding_z()


# X = int(input())
# Z = int(input())
#
# while Z <= X: # Solicita que o valor de Z seja maior que o X
#     Z = int(input())
#
# SUM = X # O valor de soma fica = ao de X, pois começamos por ele
# COUNT = 1 # Vou começar de 1 pois com a calculo X + 0 é ele mesmo
#
# while X < Z:
#     SUM = SUM + (X + 1) # Faço a seguinte conta ( 3 = 3 + 3 + 1)
#     X += 1 # Depois com isso ficaria (7 = 7 + 4 + 1)
#     COUNT += 1 # Continuo o contador
#     if SUM > Z: # Se Z for menor que a soma eu paro
#         break
# print(COUNT)

