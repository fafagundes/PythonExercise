"""
Make a program that reads five integer values. Count how many of these values ​​are even and  print this information like the following example.

Input
The input will be 5 integer values.

Output
Print a message like the following example with all letters in lowercase, indicating how many even numbers were typed.
"""

i = 0
even = 0

while i < 5:
    numbers = int(input())
    numbers = numbers % 2
    if numbers == 0:
        even = even + 1
    i = i + 1

print('{} valores pares'.format(even))
