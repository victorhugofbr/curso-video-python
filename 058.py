"""
EXERCÍCIO 058: Jogo da Adivinhação v2.0

Melhore o jogo do EXERCÍCIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""


import random

numero_random_computador = random.randint(0,10)
n_jogadas = 0

while True:
    numero_jogador = int(input("Informe um número de 0 a 10: "))

    n_jogadas += 1

    while numero_jogador < 0 or numero_jogador > 10:
        print("Número informado inválido, tente novamente! ")
        numero_jogador = int(input("Informe um número de 0 a 10: "))

    if numero_jogador == numero_random_computador:
        print(f"\nParabéns! Você escolheu {numero_jogador} e o computador escolheu {numero_random_computador}.")
        print(f"Você precisou de {n_jogadas} jogada(s) para vencer!")
        break
    else:
        print("Errado! Tente novamente.\n")