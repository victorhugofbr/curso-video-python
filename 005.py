"""
EXERCÍCIO 005: Antecessor e Sucessor

Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""


num = int(input("Informe um número inteiro: "))

ant = num - 1
suc = num + 1

print(f"Você informou o número {num}, seu antecessor é igual á {ant} e seu sucessor é o {suc}.")