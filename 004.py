"""
EXERCÍCIO 004: Dissecando uma Variável

Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""

algo = input('Digite algo: ')

print('O tipo primitivo  é: {} '.format(type(algo)))

print('Só tem espaço? {}'.format(algo.isspace()))
print(' É um número? {}'.format(algo.isnumeric()))
print('É alfabético? {}'.format(algo.isalpha()))
print('É alfanumérico? {}'.format(algo.isalnum()))
print('Está em maiúsculas? {}'.format(algo.isupper()))
print('Está em minúsculas? {}'.format(algo.islower()))
print('Está capitalizado? {}'.format(algo.istitle()))
print('A string está vazia ?',algo.isprintable())