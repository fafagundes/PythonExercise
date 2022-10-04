"""
Write an algorithm to read an undeterminated number of data, each containing an individual's age. The final data, which
will not enter in the calculations, contains the value of a negative age. Calculate and print the average age of this
group of individuals.

Input
The input contains an undetermined number of integers. The input will be stop when a negative value is read.

Output
The output contains a value corresponding to the average age of individuals.

The average should be printed with two digits after the decimal point.
"""

def ages():
    c = sum_n = n = 0

    while n >= 0:
        n = int(input())
        if n >= 0:
            sum_n += n
            c += 1

    ave = sum_n / c
    print(f"{ave:.2f}")


ages()



# SUM = 0
# C = 0
# AVE = 0
# A = int(input())
#
# while A >= 0:
#     SUM += A
#     C += 1
#     AVE = SUM / C
#     A = int(input())
# print('{:.2f}'.format(AVE))

