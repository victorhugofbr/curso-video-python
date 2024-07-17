"""
EXERCÍCIO 020: Sorteando uma Ordem na Lista

O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

import random

num1 = input("Informe o primeiro nome: ")
num2 = input("Informe o segundo nome: ")
num3 = input("Informe o terceiro nome: ")
num4 = input("Informe o quarto nome: ")

lista = [num1,num2,num3,num4]

random.shuffle(lista)

print(f"A ordem de apresentação será: {lista}")