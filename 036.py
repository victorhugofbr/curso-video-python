"""
EXERCÍCIO 036: Aprovando Empréstimo

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
"""

valor_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salário: '))
anos_pagamento = int(input('Informe em quantos anos deseja pagar a casa: '))


prestacao = (valor_casa/anos_pagamento) / 12
porcentagem_prestacao = (prestacao / salario) * 100


if prestacao > salario * 0.3:
    print('Emprestimo negado, prestação excede 30% do seu salário.')
    print(f'Valor da casa:  R${valor_casa}')
    print(f'Valor do seu salário: R${salario}')
    print(f'Valor da prestação mensal: R${prestacao:.2f} ({porcentagem_prestacao:.2f}% do salário)')
else:
    print('Emprestimo aprovado!')
    print(f'Valor da casa:  R${valor_casa}')
    print(f'Valor do seu salário: R${salario}')
    print(f'Valor da prestação mensal: R${prestacao:.2f} ({porcentagem_prestacao:.2f}% do salário)')
