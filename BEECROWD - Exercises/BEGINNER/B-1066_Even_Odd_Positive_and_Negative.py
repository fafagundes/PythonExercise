"""
Make a program that reads five integer values. Count how many   of these values are even, odd, positive and negative. Print these information like following example.

Input
The input will be 5 integer values.

Output
Print a message like the following example with all letters in lowercase, indicating how many of these values ​​are even, odd, positive and negative.
"""

def even_number():

    v_even = 0
    v_odd = 0
    v_positive = 0
    v_negative = 0
    for x in range(5):
        v_numbers = float(input())
        if v_numbers % 2 == 0:
            v_even += 1
        if v_numbers % 2 != 0:
            v_odd += 1
        if v_numbers > 0:
            v_positive += 1
        if v_numbers < 0:
            v_negative += 1

    print(f"{v_even} valor(es) par(es)")
    print(f"{v_odd} valor(es) impar(es)")
    print(f"{v_positive} valor(es) positivo(s)")
    print(f"{v_negative} valor(es) negativo(s)")


even_number()


# i = 0
# even = 0
# odd = 0
# pos = 0
# neg = 0
#
# while i < 5:
#     numbers = int(input())
#     count = numbers % 2
#     if count == 0:
#         even = even + 1
#     if count != 0:
#         odd = odd + 1
#     if numbers > 0:
#         pos = pos + 1
#     if numbers < 0:
#         neg = neg + 1
#     i = i + 1
#
# print('{} valor(es) par(es)'.format(even))
# print('{} valor(es) impar(es)'.format(odd))
# print('{} valor(es) positivo(s)'.format(pos))
# print('{} valor(es) negativo(s)'.format(neg))
