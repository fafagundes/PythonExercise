"""
Write a program that reads two scores of a student. Calculate and print the average of these scores. Your program must accept just valid scores [0..10]. Each score must be validated separately.

Input
The input file contains many floating-point numbers​​, positive or negative. The program execution will be finished after the input of two valid scores.

Output
When an invalid score is read, you should print the message "nota invalida".
After the input of two valid scores, the message "media = " must be printed followed by the average of the student. The average must be printed with 2 numbers after the decimal point.
"""


soma = 0
c = 0

a = float(input())

while(True):
    if a >= 0 and a <= 10:
        soma += a
        c += 1
        if c == 2:
            media = soma / 2
            print('media = {:.2f}'.format(media))
            break
    else:
        print('nota invalida')
    a = float(input())
