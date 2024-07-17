"""
EXERCÍCIO 018: Seno, Cosseno e Tangente

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
import math

angulo_graus = float(input('Informe um ângulo qualquer em graus: '))

angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f"Seno({angulo_graus}º) = {seno:.2f}")
print(f"Cosseno({angulo_graus}º) = {cosseno:.2f}")
print(f"Tangente({angulo_graus}º) = {tangente:.2f}")
