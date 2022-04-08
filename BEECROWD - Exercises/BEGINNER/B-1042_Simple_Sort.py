"""
Read three integers and sort them in ascending order. After, print these values in ascending order, a blank line and then the values in the sequence as they were readed.

Input
The input contains three integer numbers.

Output
Present the output as requested above.
"""

a, b, c = list(map(int, input().split()))

if a < b and b < c:
    print('{}\n{}\n{}\n'.format(a, b, c))

elif a < c and c < b:
    print('{}\n{}\n{}\n'.format(a, c, b))

elif b < a and a < c:
    print('{}\n{}\n{}\n'.format(b, a, c))

elif b < c and c < a:
    print('{}\n{}\n{}\n'.format(b, c, a))

elif c < a and a < b:
    print('{}\n{}\n{}\n'.format(c, a, b))

elif c < b and b < a:
    print('{}\n{}\n{}\n'.format(c, b, a))

print('{}\n{}\n{}'.format(a, b, c))
