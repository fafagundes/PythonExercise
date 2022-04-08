"""
Read 6 values that can be floating point numbers. After, print how many of them were positive. In the next line, print the average of all positive values typed, with one digit after the decimal point.

Input
The input consist in 6 numbers that can be integer or floating point values. At least one number will be positive.

Output
The first output value is the amount of positive numbers. The next line should show the average of the positive values ​typed.
"""

positivos = 0
i = 0
average = 0

while i < 6:
    a = float(input())
    if a > 0:
        positivos = positivos + 1
        average = average + a # Aqui ele vai acrescentar 0 + o número positivo e depois fazer o mesmo até zerar o contador
    i = i + 1
print("{} valores positivos".format(positivos))
print("{:.f}".format(average/positivos))
