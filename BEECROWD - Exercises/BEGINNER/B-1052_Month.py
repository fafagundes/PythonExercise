"""
Read an integer number between 1 and 12, including. Corresponding to this number, you must print the month of the year, in english, with the first letter in uppercase.

Input
The input contains only an integer number.

Output
Print the name of the month according to the input number, with the first letter in uppercase.
"""
mes = int(input())

if (mes<=12 and mes>0):
    if mes == 1:
        print('January')
    if mes == 2:
        print('February')
    if mes == 3:
        print('March')
    if mes == 4:
        print('April')
    if mes == 5:
        print('May')
    if mes == 6:
        print('June')
    if mes == 7:
        print('July')
    if mes == 8:
        print('August')
    if mes == 9:
        print('September')
    if mes == 10:
        print('October')
    if mes == 11:
        print('November')
    if mes == 12:
        print('December')
