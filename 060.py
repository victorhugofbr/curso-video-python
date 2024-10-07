"""
EXERCÍCIO 060: Cálculo do Fatorial

Faça um programa que leia um número qualquer e mostre seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

# Entrada do número
numero = int(input('Digite um número para calcular seu fatorial: '))
cont = numero
fatorial = 1

print(f'Calculando {numero}! = ', end='')

while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1

print(f'{fatorial}')
