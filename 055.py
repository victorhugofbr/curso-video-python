"""
EXERCÍCIO 055: Maior e Menor da Sequência

Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""

maior = 0
menor = 0
for pessoa in range(5):
    peso = float(input("Informe seu peso em kg: "))

    if pessoa == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f"o maior  peso lido foi de {maior}")
print(f'O menor peso lido foi de {menor}')