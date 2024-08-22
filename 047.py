"""
EXERCÍCIO 047: Contagem de Pares

Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""

print("*"*30)
print("Números pares no intervalo de 1 a 50.")

for numero in range(1,51):
    if numero % 2 == 0:
        print(numero,end=' ')
