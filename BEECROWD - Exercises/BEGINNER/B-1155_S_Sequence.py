"""
Write an algorithm to calculate and write the value of S, S being given by:
S = 1 + 1/2 + 1/3 + … + 1/100

Input
There is no input in this problem.

Output
The output contains a value corresponding to the value of S.
The value should be printed with two digits after the decimal point.
"""

def s_sequence():
    s = 1
    for i in range(2, 101):
        s = s + (1/i)
    print(f"{s:.2f}")


s_sequence()


# S = int(0)
#
# for i in range(1,101):
#     S = S + (1/i)
#
# print(round(S,2))
