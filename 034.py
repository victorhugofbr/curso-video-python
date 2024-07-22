"""
EXERCÍCIO 034: Aumentos Múltiplos

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Informe um número qualquer: '))

if salario > 1250:
    aumento = salario + (salario * 0.10)

else:
    aumento = salario + (salario * 0.15)


print(f'O salário anterior era de R${salario} e agora é de R${aumento}')
