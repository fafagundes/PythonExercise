"""
A gas station wants to determine which of their products is the preference of their customers. Write a program to read the type of fuel supplied (coded as follows: 1. Alcohol 2. Gasoline 3. Diesel 4. End). If you enter an invalid code (outside the range of 1 to 4) a new code must be requested. The program will end when the inserted code is the number 4.

Input
The input contains only integer and positive values.

Output
It should be written the message: "MUITO OBRIGADO" and the amount of customers who fueled each fuel type, as an example.
"""
def type_of_fuel():

    v_option = 0
    v_alcohol = v_gasoline = v_diesel = 0

    while v_option != 4:
        v_option = int(input())

        if v_option == 1:
            v_alcohol += 1
        elif v_option == 2:
            v_gasoline += 1
        elif v_option == 3:
            v_diesel += 1

    print(f"MUITO OBRIGADO")
    print(f"Alcool: {v_alcohol}")
    print(f"Gasolina: {v_gasoline}")
    print(f"Diesel: {v_diesel}")


type_of_fuel()


# alco = gaso = dies = 0
#
# INF = 0
# while(True):
#     if INF == 1:
#         alco += 1
#     elif INF == 2:
#         gaso += 1
#     elif INF == 3:
#         dies += 1
#     elif INF == 4:
#         break
#     elif INF == 0 or INF > 4:
#         INF = 0
#     INF = int(input())
# print('MUITO OBRIGADO')
# print('Alcool: {}'.format(alco))
# print('Gasolina: {}'.format(gaso))
# print('Diesel: {}'.format(dies))
