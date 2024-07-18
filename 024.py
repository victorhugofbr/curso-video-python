"""
EXERCÍCIO 024: Verificando as Primeiras Letras de um Texto

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""


cidade = input('Informe o nome da cidade: ').upper()

if cidade.split()[0] == 'SANTO':
    print(f'A cidade {cidade} começa com "SANTO"!')

else:
    print(f'A cidade {cidade} não começa com "SANTO".')
