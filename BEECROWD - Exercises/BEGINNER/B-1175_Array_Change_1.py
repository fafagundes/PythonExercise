"""
Write a program that reads an array N [20]. After, change the first element by the last,
 the second element by the last but one, etc.., Up to change the 10th to the 11th.
  print the modified array.

Input
The input contains 20 integer numbers, positive or negative.

Output
For each position of the array N print "N[i] = Y", where i is the array position
 and Y is the number stored in that position.
"""

def array_change_1():
    x = []

    for i in range(20):
        value = int(input())
        x.insert(i, value)

    x.reverse()
    for i in range(20):
        print(f"N[{i}] = {x[i]}")


array_change_1()
