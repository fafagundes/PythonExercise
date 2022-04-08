from math import sqrt, pow

x1, y1 = list(map(float, input('Enter point x and y: ').split(" ")))
x2, y2 = list(map(float, input('Enter a second point x and y: ').split(" ")))

Distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print('{:.4f}'.format(Distance))
# print(f"{distance:.4f}")
