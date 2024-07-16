"""
EXERCÍCIO 008: Conversor de Medidas

Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

medida = float(input("Informe um valor em metros: "))

cent = medida * 100
mili = medida * 1000

print(f"Você informou o valor de {medida} metros, que convertendo para centímetros terá o resultado de {cent}cm e "
      f"milímetros {mili}mm.")