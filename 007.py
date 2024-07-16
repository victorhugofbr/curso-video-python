"""
EXERCÍCIO 007: Média Aritmética

Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

nota1 = float(input("Informe sua primeira nota: "))
nota2 = float(input("Informe sua segunda nota: "))

media = (nota1 + nota2)/2

print(f"O aluno obteve na avaliação 1 a nota de {nota1}, na segunda avaliação obteve nota {nota2} e por fim, média de "
      f"{media}")
