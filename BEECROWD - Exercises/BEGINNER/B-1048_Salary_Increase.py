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

salary: float = float(input())

if 0 <= salary <= 400:
    increase = salary * 0.15
    salary = salary + increase
    percent = 15
elif 400 < salary <= 800:
    increase = salary * 0.12
    salary = salary + increase
    percent = 12
elif 800 < salary <= 1200:
    increase = salary * 0.10
    salary = salary + increase
    percent = 10
elif 1200 < salary <= 2000:
    increase = salary * 0.07
    salary = salary + increase
    percent = 7
else:
    increase = salary * 0.04
    salary = salary + increase
    percent = 4

print(f"Novo salario: {salary:.2f}")
print(f"Reajuste ganho: {increase:.2f}")
print(f"Em percentual: {percent} %")
