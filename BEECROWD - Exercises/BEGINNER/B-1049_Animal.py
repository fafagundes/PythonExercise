"""
In this problem, your job is to read three Portuguese words. These words define an animal according to the table below, from left to right. After, print the chosen animal defined by these three words.

****As opções são as que estão em cada "if"

Input
The input contains 3 words, one by line, that will be used to identify the animal, according to the above table, with all letters in lowercase.

Output
Print the animal name according to the given input.
"""

op1 = str(input())
op2 = str(input())
op3 = str(input())

if op1 == "vertebrado" and op2 == "ave" and op3 == "carnivoro":
    print("aguia")

if op1 == "vertebrado" and op2 == "ave" and op3 == "onivoro":
    print("pomba")

if op1 == "vertebrado" and op2 == "mamifero" and op3 == "onivoro":
    print("homem")

if op1 == "vertebrado" and op2 == "mamifero" and op3 == "herbivoro":
    print("vaca")

if op1 == "invertebrado" and op2 == "inseto" and op3 == "hematofago":
    print("pulga")

if op1 == "invertebrado" and op2 == "inseto" and op3 == "herbivoro":
    print("lagarta")

if op1 == "invertebrado" and op2 == "anelideo" and op3 == "hematofago":
    print("sanguessuga")

op1 = str(input())
op2 = str(input())
op3 = str(input())

lista = [op1, op2, op3]
aguia = ["vertebrado", "ave", "carnivoro"]
pomba = ["vertebrado", "ave", "onivoro"]
homem = ["vertebrado", "manifero", "onivoro"]
vaca = ["vertebrado", "manifero", "herbivoro"]
pulga = ["invertebrado", "inseto", "hematofago"]
lagarta = ["invertebrado", "inseto", "herbivoro"]
sanguessuga = ["invertebrado", "anelideo", "hematofago"]
minhoca = ["invertebrado", "anelideo", "onivoro"]

if lista == aguia:
    print("aguia")
elif lista == pomba:
    print("pomba")
elif lista == homem:
    print("homem")
elif lista == vaca:
    print("vaca")
elif lista == pulga:
    print("pulga")
elif lista == lagarta:
    print("lagarta")
elif lista == sanguessuga:
    print("sanguessuga")
else:
    print("minhoca")