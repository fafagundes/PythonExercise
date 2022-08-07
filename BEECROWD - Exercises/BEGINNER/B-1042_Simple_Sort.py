"""
Read three integers and sort them in ascending order. After, print these values in ascending order, a blank line and then the values in the sequence as they were readed.

Input
The input contains three integer numbers.

Output
Present the output as requested above.
"""

a, b, c = list(map(int, input().split()))

numbers = [a, b, c]
numbers_sorted = sorted(numbers)

for L1 in range(len(numbers_sorted)):
    print(f"{numbers_sorted[L1]}")
print()
for L2 in range(len(numbers)):
    print(f"{numbers[L2]}")
