"""
Read four numbers (N1, N2, N3, N4), which one with 1 digit after the decimal point, corresponding to 4 scores obtained by a student. Calculate the average with weights 2, 3, 4 e 1 respectively, for these 4 scores and print the message "Media: " (Average), followed by the calculated result. If the average was 7.0 or more, print the message "Aluno aprovado." (Approved Student). If the average was less than 5.0, print the message: "Aluno reprovado." (Reproved Student). If the average was between 5.0 and 6.9, including these, the program must print the message "Aluno em exame." (In exam student).

In case of exam, read one more score. Print the message "Nota do exame: " (Exam score) followed by the typed score. Recalculate the average (sum the exam score with the previous calculated average and divide by 2) and print the message “Aluno aprovado.” (Approved student) in case of average 5.0 or more) or "Aluno reprovado." (Reproved student) in case of average 4.9 or less. For these 2 cases (approved or reproved after the exam) print the message "Media final: " (Final average) followed by the final average for this student in the last line.

Input
The input contains four floating point numbers that represent the students' grades.

Output
Print all the answers with one digit after the decimal point.
"""

N1, N2, N3, N4 = list(map(float, input().split()))

MEDIA = ((N1 * 2) + (N2 * 3) + (N3 * 4) + N4) / 10

if MEDIA >= 7:
    print(f"Aluno aprovado.")
elif 7 > MEDIA >= 5:
    print(f"Aluno em exame.")
    EXAME = float(input())
    print(f"Nota do exame: {EXAME:.1f}")
    N_EXAME = (MEDIA + EXAME) / 2
    if N_EXAME >= 5:
        print(f"Aluno aprovado.")
    else:
        print(f"Aluno reprovado.")
    print(f"Media final: {N_EXAME:.1f}")
else:
    print(f"Aluno reprovado.")

"O que foi aprovado:"

ns = (input('')).split()
a = float(ns[0])
b = float(ns[1])
c = float(ns[2])
d = float(ns[3])
m = ((a * 2) + (b * 3) + (c * 4) + (d)) / 10
print('Media: {:.1f}'.format(m))
if m >= 7.0:
    print('Aluno aprovado.')
elif m < 5.0:
    print('Aluno reprovado.')
elif m >= 5.0 and m <= 6.9:
    print('Aluno em exame.')
    ne = float(input(''))
    print('Nota do exame: {:.1f}'.format(ne))
    m = (ne + m) / 2
    if m >= 5.0:
        print('Aluno aprovado.')
    elif m <= 4.9:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(m))
