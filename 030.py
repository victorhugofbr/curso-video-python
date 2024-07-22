"""
EXERCÍCIO 030: Par ou Ímpar?

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

n = int(input("Informe um número inteiro: "))

if n % 2 == 0:
    print(f"O valor {n} é PAR.")
else:
    print(f"O valor {n} é IMPAR.")
