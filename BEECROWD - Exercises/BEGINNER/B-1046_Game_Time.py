"""
Read the start time and end time of a game, in hours. Then calculate the duration of the game, knowing that the game can begin in a day and finish in another day, with a maximum duration of 24 hours. The message must be printed in portuguese “O JOGO DUROU X HORA(S)” that means “THE GAME LASTED X HOUR(S)”

Input
Two integer numbers representing the start and end time of a game.

Output
Print the duration of the game as in the sample output.
"""

A, B = list(map(int, input().split()))

if A == B:
    hour = 24
elif A > B:
    hour = 24 - (A - B)
else:
    hour = B - A

print(f"O JOGO DUROU {hour} HORA(S)")
