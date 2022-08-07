"""
Write a program that reads 6 numbers. These numbers will only be positive or negative (disregard null values). Print the total number of positive numbers.

Input
Six numbers, positive and/or negative.

Output
Print a message with the total number of positive numbers.
"""

count = 0
for number in range(0, 6):
    value = float(input())
    if value > 0:
        count = count + 1

print(f"{count} valores positivos")
