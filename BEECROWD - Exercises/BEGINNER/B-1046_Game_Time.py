"""
Read the start time and end time of a game, in hours. Then calculate the duration of the game, knowing that the game can begin in a day and finish in another day, with a maximum duration of 24 hours. The message must be printed in portuguese “O JOGO DUROU X HORA(S)” that means “THE GAME LASTED X HOUR(S)”

Input
Two integer numbers representing the start and end time of a game.

Output
Print the duration of the game as in the sample output.
"""

H1, H2 = list(map(int, input().split()))

if H1 > H2:
    HOURS = (24 - H1) + H2
else:
    if H1 < H2:
        HOURS = H2 - H1
    if H1 == H2 or H2 == H1:
        HOURS = 24
print('O JOGO DUROU {} HORA(S)'.format(HOURS))
