"""
EXERCÍCIO 033: Maior e Menor Valores

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
numero3 = int(input('Informe o terceiro número: '))


if (numero1 > numero2) and (numero1 > numero3):
    print(f'O número {numero1} é o maior.')

elif (numero2 > numero3) and (numero2 > numero1):
    print(f'O número {numero2} é o maior.')

else:
    print(f'O número {numero3} é o maior')