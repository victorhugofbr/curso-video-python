"""
EXERCÍCIO 057: Validação de Dados

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = input("Informe seu sexo (M/F): ").strip().upper()

while sexo not in "MF":
    print("Informe um sexo válido!")
    sexo = input("Informe seu sexo (M/F): ").strip().upper()

print(f'Sexo {sexo} registrado com sucesso!')