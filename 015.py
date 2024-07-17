"""
EXERCÍCIO 015: Aluguel de Carros

Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""

km_pecorridos = float(input("Informe a quantidade de km pecorridos: "))
dias_aluguel = int(input("Informe a quantidade de dias de alugel: "))

preço_alugel = 60
preço_km = 0.15

pagamento = (preço_alugel * dias_aluguel) + (preço_km * km_pecorridos)

print(f"O preço total será de R${pagamento}")