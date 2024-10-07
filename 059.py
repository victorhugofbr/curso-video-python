"""
EXERCÍCIO 059: Criando um Menu de Opções

Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:

[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

import time

primeiro_valor = int(input("Informe um número inteiro qualquer: "))
segundo_valor = int(input("Informe mais um número inteiro qualquer: "))

print("""
MENU DE OPÇÕES
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
""")

while True:
    opcao = int(input("Informe sua opção: "))

    if opcao == 1:
        soma_valores = primeiro_valor + segundo_valor
        print(f"A soma dos valores {primeiro_valor} + {segundo_valor} = {soma_valores}")

    elif opcao == 2:
        multiplicacao_valores = primeiro_valor * segundo_valor
        print(f"A multiplicação de {primeiro_valor} * {segundo_valor} = {multiplicacao_valores}")

    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print(f"O maior número informado foi {primeiro_valor}")

        else:
            print(f"O maior número informado foi {segundo_valor}")

    elif opcao == 4:
        primeiro_valor = int(input("Informe um número inteiro qualquer: "))
        segundo_valor = int(input("Informe mais um número inteiro qualquer: "))

    elif opcao == 5:
        print("Saindo do programa", end='')
        for i in range(3):
            time.sleep(0.5)
            print(".", end=' ')
        print("\nPrograma encerrado.")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")

