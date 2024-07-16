"""
EXERCÍCIO 010: Conversor de Moedas

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.

Considere U$ 1,00 = R$ 5,45
"""

dinheiro = float(input('Informe o valor em reais que você tem na carteira: '))

dolarizado = dinheiro / 5.45

print(f'Você tem R${dinheiro:.4} Reais ou ${dolarizado:.4} Dolares')