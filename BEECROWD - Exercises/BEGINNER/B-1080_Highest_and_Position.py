"""
Read 100 integer numbers. Print the highest read value and the input position.

Input
The input file contains 100 distinct positive integer numbers.

Output
Print the highest number read and the input position of this value, according to the given example.
"""

maior = 0
x = 0

for c in range(1, 101):
    n = int(input())
    if c == 1:
        maior = n
    else:
        if n > maior:
            maior = n
            x = c

print(maior)
print(x)
