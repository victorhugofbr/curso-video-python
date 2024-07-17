"""
EXERCÍCIO 011: Pintando Parede

Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
"""

largura = float(input("Informe a largura da parade (em metros): "))
altura = float(input("Informe a altura da parede (em metros): "))

area = largura * altura

tinta = area / 2

print(f"A área da parede é de {area:.2f} m².")
print(f"Será necessário {tinta:.2f} litros de tinta para pintá-la.")