"""
EXERCÍCIO 025: Procurando uma String Dentro de Outra

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

nome = input('Informe seu nome completo: ').upper().strip()

if "SILVA" in nome.split():
    print(f'O nome {nome} tem "SILVA!"')

else:
    print(f'O nome {nome} não tem "SILVA".')

