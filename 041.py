"""
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 25 anos: sênior
acima de 25: master
"""

import datetime

ano_atual = datetime.date.today().year
ano_nascimento = int(input("Informe seu ano de nascimento: "))
idade = ano_atual - ano_nascimento

print("*" * 30)
print(f"Você tem {idade} anos de idade.")

if idade <= 9:
    print("Sua Categoria é Mirim.")

elif 9 < idade <= 14:
    print("Sua Categoria é Infantil.")

elif 14 < idade <= 19:
    print("Sua Categoria é Junior.")

elif 19 < idade <= 25:
    print("Sua Categoria é Sênior.")

else:
    print("Sua Categoria é Master.")

print("*" * 30)
