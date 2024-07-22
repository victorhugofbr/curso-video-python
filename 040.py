"""
EXERCÍCIO 040: Aquele Clássico da Média

Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""

nota1 = float(input('Informe a nota da sua primeira prova: '))
nota2 = float(input('Informe a nota da sua segunda prova: '))

media = (nota1 + nota2) / 2

print(f'Sua média foi de: {media:.1f}')

if media >= 7:
    print('Aprovado!')
elif 5 <= media < 7:
    print('Recuperação')
else:
    print('Reprovado')
