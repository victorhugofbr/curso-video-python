'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, e acordo com a tabela abaixo:

- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida
'''


# Solicita o peso e a altura da pessoa
peso = float(input("Informe seu peso (em kg): "))
altura = float(input("Informe sua altura (em metros): "))

imc = peso / (altura ** 2)

print("*" * 30)
print(f"Seu IMC é de {imc:.2f}.")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está com peso ideal.")
elif 25 <= imc < 30:
    print("Você está com sobrepeso.")
elif 30 <= imc < 40:
    print("Você está com obesidade.")
else:
    print("Você está com obesidade mórbida.")

print("*" * 30)
