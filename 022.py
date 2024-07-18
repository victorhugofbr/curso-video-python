"""
EXERCÍCIO 022: Analisador de Textos

Crie um programa que leia o nome completo de uma pessoa e mostre:

> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
"""


nome_completo = input("Informe seu nome completo: ")

print(f"O nome com todas as letras maiúsculas {nome_completo.upper()}")
print(f"O nome com todas as letras minúsculas {nome_completo.lower()}")
print(f"Quantas letras tem o nome ao todo: {len(nome_completo.replace(" ",""))}")
print(f"Quantas letras tem o primeiro nome: {len(nome_completo.split()[0])}")