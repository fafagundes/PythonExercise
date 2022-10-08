"""
Mariazinha wants to solve an interesting problem. Given the population and growing rate of 2 cities (A and B),
she would like to know how many years would be necessary to the smaller city (always A) to be greater
than the larger city (always B) in population. Of course, she only wants to know the result for cities
that the growing rate for city A is bigger than the growing rate for city B, therefore, she separated
these test cases for you. Your job is to build a program that print the time in years for each test case.

However, in some cases the time can be so big and Mariazinha don't want to know the exact time for these cases.
In this way, for these test cases, it is enough printing the message "Mais de 1 seculo", that means
"More than a Century".

Input
The first line of the input contains a single integer T, indicating the number of test cases (1 ≤ T ≤ 3000).
Each test case contains four numbers: two integers PA and PB (100 ≤ PA ≤ 1000000, 100 ≤ PB ≤ 1000000, PA < PB)
indicating respectively the population of A and B and two numbers G1 and G2 (0.1 ≤ G1 ≤ 10.0, 0.0 ≤ G2 ≤ 10.0, G2 < G1)
with one digit after the decimal point each, indicating the populational growing (in percentual)
for A and B respectively.

Pay attention please: The population always is an integer number. So, a growing of 2.5% over a population of 100
will result in 102 (instead of 102.5) and a growing of 2.5% over a population of 1000 will result in 1025.
In addition, use double variables to the growing rate.

Output
Print, for each test case, how many years would be necessary to the city A became greater than the city B (in inhabitants).
Remember that if this time is greater than 100 it will be necessary printing the message: "Mais de 1 seculo".
In each one of these cases, maybe would be interesting interrupt the counting, otherwise you'll get "Time Limit Exceeded".
"""

def population_increase(n):
    for i in range(n):
        pa, pb, ga, gb = list(map(float, input().split()))
        pa = int(pa)
        pb = int(pb)

        years = 0
        while pb >= pa:
            pa = int((((ga / 100) * pa) + pa))
            pb = int((((gb / 100) * pb) + pb))
            years += 1
        if years > 100:
            print(f"Mais de 1 seculo.")
        else:
            print(f"{years} anos.")


population_increase(int(input()))


# from math import floor #Para não ter números com casa decimais
#
# T = int(input())
#
# for c in range(0, T):
#     PA, PB, G1, G2 = input().split()
#     PA = int(PA)
#     PB = int(PB)
#     G1 = float(G1)
#     G2 = float(G2)
#     y = 1
#     while True:
#         PA += floor(PA * (G1 / 100))
#         PB += floor(PB * (G2 / 100))
#         print(f"{PA} - {PB}")
#         if y > 100:
#             print('Mais de 1 seculo.')
#             break
#         if PA > PB:
#             print('{} anos.'.format(y))
#             break
#         y += 1
