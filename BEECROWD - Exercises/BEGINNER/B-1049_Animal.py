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
