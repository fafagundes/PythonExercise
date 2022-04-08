"""
Read an integer value corresponding to a person's age (in days) and print it in years, months and days, followed by its respective message “ano(s)”, “mes(es)”, “dia(s)”.

Note: only to facilitate the calculation, consider the whole year with 365 days and 30 days every month. In the cases of test there will never be a situation that allows 12 months and some days, like 360, 363 or 364. This is just an exercise for the purpose of testing simple mathematical reasoning.

Input
The input file contains 1 integer value.

Output
Print the output, like the following example.
"""

var_Number_day = int(input())

var_Years = var_Number_day // 365
var_Months = (var_Number_day % 365) // 30
var_Days = (var_Number_day % 365) % 30

print(f"{var_Years} ano(s)")
print(f"{var_Months} mes(es)")
print(f"{var_Days} dia(s)")
