"""
The company ABC decided to give a salary increase to its employees, according to the following table:


Salary	            | Readjustment Rate
0 - 400.00          | 15%
400.01 - 800.00     | 12%
800.01 - 1200.00    | 10%
1200.01 - 2000.00   | 7%
Above 2000.00       | 4%

Read the employee's salary, calculate and print the new employee's salary, as well the money earned and the increase percentual obtained by the employee, with corresponding messages in Portuguese, as the below example.
Input
The input contains only a floating-point number, with 2 digits after the decimal point.

Output
Print 3 messages followed by the corresponding numbers (see example) informing the new salary, the among of money earned and the percentual obtained by the employee. Note:
Novo salario:  means "New Salary"
Reajuste ganho: means "Money earned"
Em percentual: means "In percentage"
"""

salary = float(input())

earned = 0
percent = 0

if salary > 0 and salary <= 400.00:
    earned = salary * (15/100)
    percent = 15
elif salary >= 400.01 and salary <= 800.00:
    earned = salary * (12/100)
    percent = 12
elif salary >= 800.01 and salary <= 1200.00:
    earned = salary * (10/100)
    percent = 10
elif salary >= 1200.01 and salary <= 2000.00:
    earned = salary * (7/100)
    percent = 7
elif salary > 2000.00:
    earned = salary * (4/100)
    percent = 4

print('Novo salario: {:.2f}'.format(salary + earned))
print('Reajuste ganho: {:.2f}'.format(earned))
print('Em percentual: {} %'.format(percent))
