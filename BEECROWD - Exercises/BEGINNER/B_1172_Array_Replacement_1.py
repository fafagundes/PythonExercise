"""
Read an array X[10]. After, replace every null or negative number of X ​by 1.
Print all numbers stored in the array X.

Input
The input contains 10 integer numbers. These numbers ​​can be positive or negative.

Output
For each position of the array, print "X [i] = x", where i is the position of the array and
 x is the number stored in that position.
"""


def array_replacement_1():
    X = []
    for i in range(10):
        value = int(input())
        if value <= 0:
            value = 1
            X.insert(i, value)
        else:
            X.insert(i, value)

    for i in range(10):
        print(f"X[{i}] = {X[i]}")


array_replacement_1()
