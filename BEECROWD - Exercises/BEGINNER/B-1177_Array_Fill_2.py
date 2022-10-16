"""
Write a program that reads a number T and fill a vector N[1000] with the numbers
from 0 to T-1 repeated times, like as the example below.

Input
The input contains an integer number T (2 ≤ T ≤ 50).

Output
For each position of the array N, print "N[i] = x", where i is the array
position and x is the number stored in that position.
"""

def array_fill_2(t):
    n = 0
    array_list = []
    while n <= 1000:
        for i in range(t):
            array_list.append(i)
            n += 1
    for j in range(1000):
        print(f"N[{j}] = {array_list[j]}")


array_fill_2(int(input()))
