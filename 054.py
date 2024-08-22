"""
EXERCÍCIO 054: Grupo de Maioridade

Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date

ano_atual = date.today().year

de_maior = 0
de_menor = 0
for pessoa in range(7):
    ano_nascimento = int(input("Informe o ano de nascimento: "))
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        de_maior += 1
    else:
        de_menor += 1

print(f"Há {de_maior} maiores de idade e {de_menor} menores de idade.")