"""
In this problem, your task is to read an array A[100]. At the end, print all array positions
 that store a number less or equal to 10 and the number stored in that position.

Input
The input contains 100 numbers. Each number can be integer, floating-point number, positive or negative.

Output
For each number of the array that is equal to 10 or less, print "A [i] = x", where i is the position
 of the array and x is the number stored in the position, with one digit after the decimal point.
"""


def array_selection_1():
    x = []

    for i in range(100):
        value = float(input())
        x.insert(i, value)

    for i in range(100):
        if x[i] <= 10:
            print(f"A[{i}] = {x[i]:.1f}")


array_selection_1()
