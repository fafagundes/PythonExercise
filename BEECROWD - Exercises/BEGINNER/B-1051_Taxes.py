"""
In an imaginary country called Lisarb, all the people are very happy to pay their taxes because they know that doesn’t exist corrupt politicians and the taxes are used to benefit the population, without any misappropriation. The currency of this country is Rombus, whose symbol is R$.

Read a value with 2 digits after the decimal point, equivalent to the salary of a Lisarb inhabitant. Then print the due value that this person must pay of taxes, according to the table below.

=====================================================
Salario de 0 a 2000.00 - Sem taxas
Salario de 2000.01 até 3000.00 - 8%
Salario de 3000.01 até 4500.00 - 18%
Salario acima de 4500.01 - 28%
=====================================================

Remember, if the salary is R$ 3,002.00 for example, the rate of 8% is only over R$ 1,000.00, because the salary from R$ 0.00 to R$ 2,000.00 is tax free. In the follow example, the total rate is 8% over R$ 1000.00 + 18% over R$ 2.00, resulting in R$ 80.36 at all. The answer must be printed with 2 digits after the decimal point.

Input
The input contains only a float-point number, with 2 digits after the decimal point.

Output
Print the message "R$" followed by a blank space and the total tax to be payed, with two digits after the decimal point. If the value is up to 2000, print the message "Isento".
"""

salary = float(input())

if salary > 0 and salary <= 2000.00:
    print('Isento')
elif salary >= 2000.01 and salary <= 3000.00:
    salary = salary - 2000.00
    taxa = salary * (8/100)
    print('R$ {:.2f}'.format(taxa))
elif salary >= 3000.01 and salary <= 4500.00:
    t18 = salary - 3000.01
    t8 = salary - 2000.01 - t18
    print(t18)
    print(t8)
    tx18 = t18 * (18/100)
    tx8 = t8 * (8/100)
    taxa = tx8 + tx18
    print('R$ {:.2f}'.format(taxa))
elif salary > 4500.00:
    t28 = salary - 4500.00
    t18 = salary - 3000.01 - t28
    t8 = salary - 2000.01 - t28 - t18
    tx28 = t28 * (28 / 100)
    tx18 = t18 * (18 / 100)
    tx8 = t8 * (8 / 100)
    taxa = tx28 + tx18 + tx8
    print('R$ {:.2f}'.format(taxa))

# O de baixo é o que foi aceito

d = float(input())
p1 = 0
p2 = 0
p3 = 0
if d <= 2000.00:
    print('Isento')
elif 2000.01 <= d <= 3000:
    p1 = d - 2000.0
elif 3000.01 <= d <= 4500:
    p1 = 1000
    p2 = d - 3000.0
else:
    p1 = 1000
    p2 = 1500
    p3 = d - 4500.0

if p1 != 0:
    print('R$ {:.2f}'.format(p1*8/100+p2*18/100+p3*28/100))