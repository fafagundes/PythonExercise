"""
Read the start time and end time of a game, in hours and minutes (initial hour, initial minute, final hour, final minute). Then print the duration of the game, knowing that the game can begin in a day and finish in another day,

Obs.: With a maximum game time of 24 hours and the minimum game time of 1 minute.

Input
Four integer numbers representing the start and end time of the game.

Output
Print the duration of the game in hours and minutes, in this format: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” . Which means: the game lasted XXX hour(s) and YYY minutes.
"""


H1, M1, H2, M2 = list(map(int, input().split()))

t1 = 60 * M1 + 3600 * H1
dur = (24 * 3600) - t1
t2 = 60 * M2 + 3600 * H2
dur += t2
hd = dur//3600
dur = dur%3600
md = dur//60

if hd >= 24:
    hd = hd - 24
if H1 == H2:
    hd = 24

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hd, md))
