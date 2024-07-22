"""
EXERCÍCIO 035: Analisando Triângulo v1.0

Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""

a = float(input('Informe o comprimento de "a": '))
b = float(input('Informe o comprimento de "b": '))
c = float(input('Informe o comprimento de "c": '))

if (a + b > c) and (b + c > a) and (a + c > b):
    print('Podem formar um triângulo.')

else:
    print('Não podem formar o triângulo.')