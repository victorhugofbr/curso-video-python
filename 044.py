'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''


preco_compras = float(input("Preço das compras: R$ "))

print("Selecione uma forma de pagamento:")
print('''
Digite 1: Para pagar à vista no dinheiro/cheque (10% de desconto)
Digite 2: Para pagar à vista no cartão (5% de desconto)
Digite 3: Para pagar em 2x no cartão (preço normal)
Digite 4: Para pagar em 3x ou mais no cartão (20% de juros)\n''')

opcao = int(input("Informe sua opção de pagamento: "))

if opcao == 1:
    print("Você selecionou pagamento à vista em dinheiro/cheque. Receberá 10% de desconto.")
    desconto = preco_compras * 0.10
    valor_final = preco_compras - desconto
    print(f"O valor original das compras era de R${preco_compras:.2f}. Com o desconto, será de R${valor_final:.2f}.")

elif opcao == 2:
    print("Você selecionou pagamento à vista no cartão. Receberá 5% de desconto.")
    desconto = preco_compras * 0.05
    valor_final = preco_compras - desconto
    print(f"O valor original das compras era de R${preco_compras:.2f}. Com o desconto, será de R${valor_final:.2f}.")

elif opcao == 3:
    print("Você selecionou pagamento em 2x no cartão. O preço será o normal.")
    parcela = preco_compras / 2
    print(f"O valor das compras será de R${preco_compras:.2f}, dividido em 2x de R${parcela:.2f} sem juros.")

elif opcao == 4:
    print("Você selecionou pagamento em 3x ou mais no cartão. Haverá um acréscimo de 20% de juros.")
    parcelas = int(input("Em quantas vezes você deseja parcelar? "))
    if parcelas < 3:
        print("A quantidade mínima de parcelas para esta opção é 3x no cartão.")
    else:
        acrescimo = preco_compras * 0.20
        valor_final = preco_compras + acrescimo
        parcela = valor_final / parcelas
        print(f"O valor das compras será de R${valor_final:.2f}, dividido em {parcelas}x de R${parcela:.2f} com juros.")

else:
    print("Opção inválida. Por favor, selecione uma alternativa válida.")

