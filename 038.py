"""
EXERCÍCIO 038: Comparando Números

Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
"""

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe um outro número inteiro: '))

if n1 > n2:
    print(f'O valor {n1} é maior que {n2}')

elif n2 > n1:
    print(f'O valor {n2} é maior que {n1}')

else:
    print(f'Não existe valor maior {n1} e {n2} são iguais.')
