"""
EXERCÍCIO 012: Calculando Descontos

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

produto_preco = float(input("Informe o preço do produto (em reais): "))

produto_desconto = produto_preco - (produto_preco * 5 / 100)

print(f"O preço do produto é de R${produto_preco:.2f}")
print(f"Com o desconto de 5% seu novo preço será de R${produto_desconto:.2f}")