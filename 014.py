"""
EXERCÍCIO 014: Conversor de Temperaturas

Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
"""

temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

print(f"A temperatura de {temperatura_celsius}ºC corresponde a {temperatura_fahrenheit}ºF.")
