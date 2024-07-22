"""
EXERCÍCIO 032: Ano Bissexto

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""

ano = int(input('Informe um ano: '))


if (ano % 4 == 0  and ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano} é bissexto.')

else:
    print(f'{ano} não é bissexto.')