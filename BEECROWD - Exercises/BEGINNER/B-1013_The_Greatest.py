#a, b, c = list(map(int, input().split()))
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

MaiorAB = (a + b + abs(a-b)) / 2
MaiorABC = (MaiorAB + c + abs(MaiorAB-c)) / 2

print('{} eh o maior'.format(int(MaiorABC)))
