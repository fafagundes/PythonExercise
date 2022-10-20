"""
In this problem you need to read 15 numbers and must put them into two different arrays:
par if the number is even or impar if this number is odd. But  the size of each of the
two arrrays is only 5 positions. So every time you fill one of two arrays,
you must print the entire array to be able to use it again for the next numbers that are read.
At the end, all remaining numbers of each one of these two arrays must be printed beggining
with the odd array. Each array can be filled how many times are necessary.

Input
The input contains 15 integer numbers.

Output
Print the output like the following example.
"""

# def array_fill_4():
#     even = []
#     odd = []
#     for a in range(15):
#         num = int(input())
#         if num % 2 == 0:
#             even.append(num)
#             if len(even) == 5:
#                 for num_even in range(len(even)):
#                     print(f"par[{num_even}] = {even[num_even]}")
#                 even = []
#         else:
#             odd.append(num)
#             if len(odd) == 5:
#                 for num_odd in range(len(odd)):
#                     print(f"impar[{num_odd}] = {odd[num_odd]}")
#                 odd = []
#
#     for num_odd in range(len(odd)):
#         print(f"impar[{num_odd}] = {odd[num_odd]}")
#     for num_even in range(len(even)):
#         print(f"par[{num_even}] = {even[num_even]}")
#
#
# array_fill_4()

def mostra_array(array, texto):
    for posicao, num in enumerate(array):
        print("{}[{}] = {}".format(texto, posicao, num))


pares = []
impares = []

for i in range(15):
    n = int(input())
    if n % 2 == 0:
        pares.append(n)
        if len(pares) == 5:  # mal chega aos 5 mostra e limpa
            mostra_array(pares, "par")
            pares = []

    if n % 2 != 0:
        impares.append(n)
        if len(impares) == 5:  # mal chega aos 5 mostra e limpa
            mostra_array(impares, "impar")
            impares = []

# no fim os que sobraram são escritos, começando pelo impar
mostra_array(impares, "impar")
mostra_array(pares, "par")
