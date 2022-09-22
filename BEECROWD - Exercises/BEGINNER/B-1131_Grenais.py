"""
The Federação Gaúcha de Futebol invited you to write a program to present a statistical result of several GRENAIS. Write a program that read the number of goals scored by Inter and the number of goals scored by Gremio in a GRENAL. Write the message "Novo grenal (1-sim 2-nao)" and request a response. If the answer is 1, two new numbers must be read (another input case) asking the number of goals scored by the teams in a new departure, otherwise the program must be finished, printing:

- How many GRENAIS were part of the statistics.
- The number of victories of Inter.
- The number of victories of Gremio.
- The number of Draws.
- A message indicating the team that won the largest number of GRENAIS (or the message: "Não houve vencedor" if both team won the same quantity of GRENAIS).

Input
The input contains two integer values​​, corresponding to the goals scored by both teams. Then there is an integer (1 or 2), corresponding to the repetition of the algorithm.

Output
After each reading of the goals it must be printed the message "Novo grenal (1-sim 2-nao)". When the program is finished, the program must print the statistics as the example below.
"""

def grenais():

    option = 1
    grenais = 0
    v_inter = 0
    v_gremio = 0
    empates = 0

    while option != 2:

        if option == 1:
            inter, gremio = list(map(int, input().split()))
            grenais += 1

            if inter > gremio:
                v_inter += 1
            elif inter == gremio:
                empates += 1
            else:
                v_gremio += 1

            option = int(input(f"Novo grenal (1-sim 2-nao)\n"))

    print(f"{grenais} grenais")
    print(f"Inter:{v_inter}")
    print(f"Gremio:{v_gremio}")
    print(f"Empates:{empates}")
    if v_inter > v_gremio:
        print(f"Inter venceu mais")
    elif v_inter < v_gremio:
        print(f"Gremio venceu mais")
    else:
        print(f"Não houve vencedor")

grenais()


# I, G = list(map(int, input().split()))
#
# somaG = 0
# somaI = 0
# emp = 0
# c = 1
#
#
# while(True):
#     if I > G:
#         somaI += 1
#     elif G > I:
#         somaG += 1
#     else:
#         emp += 1
#     nov = int(input('Novo grenal (1-sim 2-nao)\n'))
#     while 1 != nov != 2:
#         nov = int(input('Novo grenal (1-sim 2-nao)\n'))
#     if nov == 1:
#         c += 1
#     elif nov == 2:
#         print('{} grenais'.format(c))
#         print('Inter:{}'.format(somaI))
#         print('Gremio:{}'.format(somaG))
#         print('Empates:{}'.format(emp))
#         if somaI > somaG:
#             print('Inter venceu mais')
#         elif somaG > somaI:
#             print('Gremio venceu mais')
#         else:
#             print('Não houve vencedor')
#         break
#     I, G = list(map(int, input().split()))