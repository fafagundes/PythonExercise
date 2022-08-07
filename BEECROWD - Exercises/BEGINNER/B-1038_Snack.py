"""
Using the following table, write a program that reads a code and the amount of an item. After, print the value to pay. This is a very simple program with the only intention of practice of selection commands.

Tabela:
Code | Specification   | Price
---------------------------------
1    | Cachorro Quente | R$ 4.00
2    | X-Salada        | R$ 4.50
3    | X-Bacon         | R$ 5.00
4    | Torrada Simples | R$ 2.00
5    | Refrigerante    | R$ 1.50

Input
The input file contains two integer numbers X and Y. X is the product code and Y is the quantity of this item according to the above table.

Output
The output must be a message "Total: R$ " followed by the total value to be paid, with 2 digits after the decimal point.
"""

X, Y = list(map(int, input().split()))

if X == 1:
    X = 4.00
elif X == 2:
    X = 4.50
elif X == 3:
    X = 5.00
elif X == 4:
    X = 2.00
elif X == 5:
    X = 1.50

Total = X * Y
print(f"Total: R$ {Total:.2f}")
