"""
Read 100 integer numbers. Print the highest read value and the input position.

Input
The input file contains 100 distinct positive integer numbers.

Output
Print the highest number read and the input position of this value, according to the given example.
"""

def heighest_number():
    n_heighest = 0
    count = 0

    for c in range(1, 101):
        n = int(input())
        if c == 1:
            n_heighest = n
        else:
            if n > n_heighest:
                n_heighest = n
                count = c

    print(n_heighest)
    print(count)


heighest_number()


# def heighest_number():
#
#     numbers = []
#     heighest = 0
#     index = 0
#     for i in range(100):
#         number = int(input())
#         numbers.append(number)
#         index = numbers.index(max(numbers))+1
#         heighest = max(numbers)
#     print(heighest)
#     print(index)
#
# heighest_number()