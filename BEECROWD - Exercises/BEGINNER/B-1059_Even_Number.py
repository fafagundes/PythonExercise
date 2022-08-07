"""
Write a program that prints all even numbers between 1 and 100, including them if it is the case.

Input
In this extremely simple problem there is no input.

Output
Print all even numbers between 1 and 100, including them, one by row.
"""

for number in range(1, 100+1):
    if number % 2 == 0:
        print(number)
