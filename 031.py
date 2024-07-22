"""
EXERCÍCIO 031: Custo da Viagem

Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
"""

distancia = float(input("Informe a distância pecorrida em km: "))

if distancia <= 200:
    preco = 0.5 * distancia

else:
    preco = 0.45 * distancia

print(f'A viagem é de {distancia}km e o preço da passagem será de R${preco}')
