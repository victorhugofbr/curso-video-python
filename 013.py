"""
EXERCÍCIO 013: Reajuste Salarial

Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

salario = float(input("Informe seu salário (em reais): "))

aumento = salario + (salario * 15/100)

print(f"Seu salário antigo era de R${salario}")
print(f"Seu novo salário com aumento de 15% é de R${aumento}")