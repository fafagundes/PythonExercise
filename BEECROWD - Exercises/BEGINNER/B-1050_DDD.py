"""
Read an integer number that is the code number for phone dialing. Then, print the destination according to the following table:

61 - Brasilia
71 - Salvador
11 - Sao Paulo
21 - Rio de Janeiro
32 - Juiz de Fora
19 - Campinas
27 - Vitoria
31 - Belo Horizonte

If the input number isn’t found in the above table, the output must be:
DDD nao cadastrado
That means “DDD not found” in Portuguese language.

Input
The input consists in a unique integer number.

Output
Print the city name corresponding to the input DDD. Print DDD nao cadastrado if doesn't exist corresponding DDD to the typed number.
"""

DDD = int(input())

if DDD == 61:
    city = 'Brasilia'
    print(city)
elif DDD == 71:
    city = 'Salvador'
    print(city)
elif DDD == 11:
    city = 'Sao Paulo'
    print(city)
elif DDD == 21:
    city = 'Rio de Janeiro'
    print(city)
elif DDD == 32:
    city = 'Juiz de Fora'
    print(city)
elif DDD == 19:
    city = 'Campinas'
    print(city)
elif DDD == 27:
    city = 'Vitoria'
    print(city)
elif DDD == 31:
    city = 'Belo Horizonte'
    print(city)
else:
    print('DDD nao cadastrado')
