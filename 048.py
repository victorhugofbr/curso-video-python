"""
EXERCÍCIO 048: Soma Ímpares Múltiplos de Três

Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

soma = 0
for numero in range(1,501):
    if numero % 2 != 0:
        if numero % 3 == 0:
            soma += numero

print(f"A soma dos números impares que são múltiplos de três: {soma} ")