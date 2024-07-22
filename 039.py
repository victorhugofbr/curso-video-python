"""
EXERCÍCIO 039: Alistamento Militar

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

import datetime

currentDateTime = datetime.datetime.now()
year = currentDateTime.year

ano_nascimento = int(input('Informe seu ano de nascimento: '))
idade = year - ano_nascimento

print(f'Sua idade é {idade} anos.')

if idade < 18:
    anos_restantes = 18 - idade
    ano_alistamento = year + anos_restantes
    print(f'Ainda não é hora de se alistar. Faltam {anos_restantes} anos para o alistamento, que será em {ano_alistamento}.')
elif idade == 18:
    print('É hora de se alistar para o serviço militar.')
else:
    anos_passados = idade - 18
    ano_alistamento = year - anos_passados
    print(f'Já passou do tempo de alistamento. Você deveria ter se alistado há {anos_passados} anos, em {ano_alistamento}.')

