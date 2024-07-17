"""
EXERCÍCIO 019: Sorteando um Item na Lista

Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
import random

num1 = input("Informe o primeiro nome: ")
num2 = input("Informe o segundo nome: ")
num3 = input("Informe o terceiro nome: ")
num4 = input("Informe o quarto nome: ")

lista = [num1,num2,num3,num4]

azarado = random.choice(lista)

print(f"O azarado que foi escolhido pelo professor para fazer 100 questões de python foi o {azarado}")