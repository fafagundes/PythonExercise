"""
Read a number X. Put this X at the first position of an array N [100]. In each subsequent
position (1 up to 99) put half of the number
 inserted at the previous position, according to the example below. Print all the vector N.

Input
The input contains a double precision number with four decimal places.

Output
For each position of the array N print "N[i] = Y", where i is the array position and Y
is the number stored in that position. Each number of N[...] must be printed with
4 digits after the decimal point.
"""

def array_fill_3(t):
    array_list = [t]
    for i in range(100):
        t = t / 2
        array_list.append(t)
    for j in range(100):
        print(f"N[{j}] = {array_list[j]:.4f}")


array_fill_3(float(input()))
