"""
Read a value of floating point with two decimal places. This represents a monetary value.
After this, calculate the smallest possible number of notes and coins on which the value
can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins
are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list
of notes and the message “MOEDAS:” followed by the list of coins.

Input
The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

Output
Print the minimum quantity of banknotes and coins necessary to change the initial value,
as the given example.
"""

# N = float(input())
#
# if N > 0.00 and N < 1000000.00:
#
#     NCem = (N // 100)
#     N = N - NCem * 100
#     NCinquenta = (N // 50)
#     N = N - NCinquenta * 50
#     NVinte = (N // 20)
#     N = N - NVinte * 20
#     NDez = (N // 10)
#     N = N - NDez * 10
#     NCinco = (N // 5)
#     N = N - NCinco * 5
#     NDois = (N // 2)
#     N = N - NDois * 2
#
#     moedaUm = (N // 1)
#     N = N - moedaUm * 1
#     moedaCinquenta = (N // 0.5)
#     N = N - moedaCinquenta * 0.5
#     moedaVinteCinco = (N // 0.25)
#     N = N - moedaVinteCinco * 0.25
#     moedaDez = (N // 0.10)
#     N = N - moedaDez * 0.10
#     moedaCinco = (N // 0.05)
#     N = N - moedaCinco * 0.05
#     moedaZeroUm = (N // 0.01)
#
#     print('NS:')
#     print('{:.0f} nota(s) de R$ 100.00'.format(NCem))
#     print('{:.0f} nota(s) de R$ 50.00'.format(NCinquenta))
#     print('{:.0f} nota(s) de R$ 20.00'.format(NVinte))
#     print('{:.0f} nota(s) de R$ 10.00'.format(NDez))
#     print('{:.0f} nota(s) de R$ 5.00'.format(NCinco))
#     print('{:.0f} nota(s) de R$ 2.00'.format(NDois))
#
#     print('MOEDAS:')
#     print('{:.0f} moeda(s) de 1.00'.format(moedaUm))
#     print('{:.0f} moeda(s) de 0.50'.format(moedaCinquenta))
#     print('{:.0f} moeda(s) de 0.25'.format(moedaVinteCinco))
#     print('{:.0f} moeda(s) de 0.10'.format(moedaDez))
#     print('{:.0f} moeda(s) de 0.05'.format(moedaCinco))
#     print('{:.0f} moeda(s) de 0.01'.format(moedaZeroUm))


var_Number = float(input())

# Notes and Coins list
var_Notes_list = [100, 50, 20, 10, 5, 2]
var_Coins_list = [0.50, 0.25, 0.10, 0.05, 0.01]

var_Decimal = var_Number % 1

# Condition request
if 0 < var_Number < 1000000.00:
    # for to the first list
    print("NOTAS:")
    for list_notes in var_Notes_list:
        var_Number = int(var_Number)
        var_Result_notes = var_Number // list_notes  # Floor division
        print(f"{var_Result_notes:.0f} notas(s) de R$ {list_notes:.0f}.00")
        var_Number = var_Number % list_notes  # Modulus division

print("MOEDAS:")
if var_Number == 1:
    print(f"{var_Number:.0f} moeda(s) de R$ 1.00")
else:
    print(f"0 moeda(s) de R$ 1.00")
if var_Decimal < 1:
    var_Decimal = float(f"{var_Decimal:.2f}")
    for list_coins in var_Coins_list:

        if var_Decimal == 0.03 and list_coins == 0.01:
            var_Result_coins = 3
            print(f"{var_Result_coins:.0f} moeda(s) de R$ {list_coins:.2f}")
        else:
            var_Result_coins = var_Decimal // list_coins
            print(f"{var_Result_coins:.0f} moeda(s) de R$ {list_coins:.2f}")
            var_Decimal = var_Decimal % list_coins
            var_Decimal = float(f"{var_Decimal:.2f}")
