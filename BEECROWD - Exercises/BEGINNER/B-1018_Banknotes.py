"""
In this problem you have to read an integer value and calculate the smallest possible number of banknotes in which the value may be decomposed. The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value and the list of banknotes.

Input
The input file contains an integer value N (0 < N < 1000000).

Output
Print the read number and the minimum quantity of each necessary banknotes in Portuguese language, as the given example. Do not forget to print the end of line after each line, otherwise you will receive “Presentation Error”.
"""

var_Number = int(input())

# var_Qtd_100 = var_Number // 100  # absolute divide
# var_Qtd_50 = (var_Number % 100) // 50  # rest of divide and absolute divide
# var_Qtd_20 = ((var_Number % 100) % 50) // 20
# var_Qtd_10 = (((var_Number % 100) % 50) % 20) // 10
# var_Qtd_5 = ((((var_Number % 100) % 50) % 20) % 10) // 5
# var_Qtd_2 = (((((var_Number % 100) % 50) % 20) % 10) % 5) // 2
# var_Qtd_1 = ((((((var_Number % 100) % 50) % 20) % 10) % 5) % 2)
#
#
# print(f'{var_Number}')
# print(f"{int(var_Qtd_100)} nota(s) de R$ 100,00")
# print(f"{int(var_Qtd_50)} nota(s) de R$ 50,00")
# print(f"{int(var_Qtd_20)} nota(s) de R$ 20,00")
# print(f"{int(var_Qtd_10)} nota(s) de R$ 10,00")
# print(f"{int(var_Qtd_5)} nota(s) de R$ 5,00")
# print(f"{int(var_Qtd_2)} nota(s) de R$ 2,00")
# print(f"{int(var_Qtd_1)} nota(s) de R$ 1,00")

var_Notes = [100, 50, 20, 10, 5, 2, 1]

if 0 < var_Number < 1000000:
    print(var_Number)
    for i in var_Notes:  # the range is the list
        var_Result = var_Number // i  # make the absolute division
        print(f"{var_Result} notas(s) de R$ {i},00")
        var_Number = var_Number % i  # make the modulus division (the rest) e put inside var_Number

# var_Notes = [100, 50, 20, 10, 5, 2, 1]
# if 0 < var_Number < 1000000:
#     print(var_Number)
#     for i in var_Notes:
#         var_Notes = var_Number // i
#         print(f"{var_Notes} nota(s) de R$ {i},00")
#         var_Number -= var_Notes * i


