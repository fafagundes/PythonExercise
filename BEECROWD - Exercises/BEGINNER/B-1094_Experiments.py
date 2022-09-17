"""
Maria has just started as graduate student in a medical school and she's needing your help to organize a laboratory experiment which she is responsible about. She wants to know, at the end of the year, how many animals were used in this laboratory and the percentage of each type of animal is used at all.

This laboratory uses in particular three types of animals: frogs, rats and rabbits. To obtain this information, it knows exactly the number of experiments that were performed, the type and quantity of each animal is used in each experiment.

Input
The first line of input contains an integer N indicating the number of test cases that follows. Each test case contains an integer Amount (1 ≤ Amount ≤ 15) which represents the amount of animal used and a character Type ('C', 'R' or 'S'), indicating the type of animal:
- C: Coelho (rabbit in portuguese)
- R: Rato (rat  in portuguese)
- S: Sapo (frog in portuguese)

Output
Print the total of animals used, the total of each type of animal and the percentual of each one in relation of the total of animals used. The percentual must be printed with 2 digits after the decimal point.
"""

def experiments(n):

    v_total = 0
    v_total_habbit = 0
    v_total_rat = 0
    v_total_frog = 0

    for i in range(n):
        number, animal = list(map(str, input().split()))
        number = int(number)
        v_total += number
        if animal == "C":
            v_total_habbit += number
        elif animal == "R":
            v_total_rat += number
        elif animal == "S":
            v_total_frog += number

    v_percent_habbit = (v_total_habbit / v_total) * 100
    v_percent_rat = (v_total_rat / v_total) * 100
    v_percent_frog = (v_total_frog / v_total) * 100

    print(f"Total: {v_total} cobaias")
    print(f"Total de coelhos: {v_total_habbit}")
    print(f"Total de ratos: {v_total_rat}")
    print(f"Total de sapos: {v_total_frog}")
    print(f"Percentual de coelhos: {v_percent_habbit:.2f} %")
    print(f"Percentual de ratos: {v_percent_rat:.2f} %")
    print(f"Percentual de sapos: {v_percent_frog:.2f} %")

experiments(int(input()))


# N = int(input())
#
# COE = 0
# RAT = 0
# SAP = 0
# TOTAL = 0
#
# for c in range(0, N):
#     INF = input().split()
#     TOTAL += int(INF[0])
#     if INF[1] == 'C':
#         COE += int(INF[0])
#     elif INF[1] == 'R':
#         RAT += int(INF[0])
#     elif INF[1] == 'S':
#         SAP += int(INF[0])
#
# PCOE = (COE / TOTAL) * 100
# PRAT = (RAT / TOTAL) * 100
# PSAP = (SAP / TOTAL) * 100
#
# print('Total: {} cobaias'.format(TOTAL))
# print('Total de coelhos: {}'.format(COE))
# print('Total de ratos: {}'.format(RAT))
# print('Total de sapos: {}'.format(SAP))
# print('Percentual de coelhos: {:.2f} %'.format(PCOE))
# print('Percentual de ratos: {:.2f} %'.format(PRAT))
# print('Percentual de sapos: {:.2f} %'.format(PSAP))

