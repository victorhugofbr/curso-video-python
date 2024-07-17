"""
EXERCÍCIO 017: Catetos e Hipotenusa

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""

cateto_oposto = int(input('Informe o comprimento do cateto oposto: '))
cateto_adjacente = int(input('Informe o comprimento do cateto adjacente: '))

hipotenusa = (cateto_adjacente**2 + cateto_oposto**2)**0.5

print(f'O comprimento da hipotenusa é de : {hipotenusa}')