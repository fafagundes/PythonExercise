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

def taxes(v_Salary):

    v_Taxes_28 = 0
    v_Taxes_18 = 0
    v_Taxes_8 = 0

    if 0 <= v_Salary <= 2000.00:
        print("Isento")
    else:
        if v_Salary > 4500:
            v_Taxes_28 = (v_Salary - 4500.00) * 0.28
            v_Salary = v_Salary - (v_Salary - 4500.00)
        if 3000.01 <= v_Salary <= 4500:
            v_Taxes_18 = (v_Salary - 3000.01) * 0.18
            v_Salary = v_Salary - (v_Salary - 3000)
        if 2000.01 <= v_Salary <= 3000:
            v_Taxes_8 = (v_Salary - 2000.01) * 0.08
            v_Salary = v_Salary - (v_Salary - 2000.01)

        v_Total_Taxes = v_Taxes_28 + v_Taxes_18 + v_Taxes_8
        print(f"R$ {v_Total_Taxes:.2f}")


taxes(float(input()))

# salary = float(input())

# if salary > 0 and salary <= 2000.00:
#     print('Isento')
# elif salary >= 2000.01 and salary <= 3000.00:
#     salary = salary - 2000.00
#     taxa = salary * (8/100)
#     print('R$ {:.2f}'.format(taxa))
# elif salary >= 3000.01 and salary <= 4500.00:
#     t18 = salary - 3000.01
#     t8 = salary - 2000.01 - t18
#     print(t18)
#     print(t8)
#     tx18 = t18 * (18/100)
#     tx8 = t8 * (8/100)
#     taxa = tx8 + tx18
#     print('R$ {:.2f}'.format(taxa))
# elif salary > 4500.00:
#     t28 = salary - 4500.00
#     t18 = salary - 3000.01 - t28
#     t8 = salary - 2000.01 - t28 - t18
#     tx28 = t28 * (28 / 100)
#     tx18 = t18 * (18 / 100)
#     tx8 = t8 * (8 / 100)
#     taxa = tx28 + tx18 + tx8
#     print('R$ {:.2f}'.format(taxa))

