"""
Two friends ask the attendant a snack bar propose a challenge , so that whoever hit him more,
would not pay the bill. Then the following is proposed : Given the following sum below report
the result , with the same number of terms : S = 1 - 1 + 1 - 1 + 1 - 1 + 1 - 1 ...
Write a program that , given a number of terms, report the result of the sum above.

Input
An integer C shall be informed , which is the amount of test cases. Each test case starts
with an integer N ( 1 ≤ N ≤ 1000) , indicating the number of terms of the sum .

Output
For each test case print a number S , which is the sum of N terms of expression.

"""

c = int(input())

def test_sum(num):
    if num % 2 == 0:
        print("0")
    else:
        print("1")


for i in range(c):
    test_sum(int(input()))
