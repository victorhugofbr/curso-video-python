'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import choice
from time import sleep

lista = ["pedra", "papel", "tesoura"]

print('''
COMPUTADOR: Vamos jogar Pedra, Papel, Tesoura!
As regras são as seguintes:
- Papel vence Pedra e perde para Tesoura
- Pedra vence Tesoura e perde para Papel
- Tesoura vence Papel e perde para Pedra
''')

jogador = str(input("Você escolhe pedra, papel ou tesoura? \n")).lower()

if jogador not in lista:
    print(f"{jogador} não é uma opção válida. Escolha pedra, papel ou tesoura.")
else:
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(0.5)
    print("PÔ!!!")

    computador = choice(lista)

    print(f'''
    Jogador: {jogador.capitalize()}
    Computador: {computador.capitalize()}''')

    if jogador == computador:
        print("Empate. Vamos jogar novamente.")
    elif (jogador == "pedra" and computador == "tesoura") or \
            (jogador == "tesoura" and computador == "papel") or \
            (jogador == "papel" and computador == "pedra"):
        print("Você venceu!")
    else:
        print("Computador venceu!")
