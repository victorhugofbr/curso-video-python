"""
EXERCÍCIO 063: Sequência de Fibonacci v1.0

Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.

Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""


print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

n = int(input('Quantos termos você quer mostrar? '))

termo_um = 0
termo_dois = 1

print('~' * 30)

print(f'{termo_um} → {termo_dois}', end='')

for _ in range(3, n + 1):
    termo_tres = termo_um + termo_dois
    print(f' → {termo_tres}', end='')
    termo_um = termo_dois
    termo_dois = termo_tres

print(' → FIM')
