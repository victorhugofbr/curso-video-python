"""
EXERCÍCIO 056: Analisador Completo

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""

soma_idade = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ""
mulheres_menores_20 = 0

for pessoa in range(1, 5):
    nome = input(f"Informe o nome da pessoa {pessoa}: ")
    idade = int(input(f"Informe a idade da pessoa {pessoa}: "))

    while True:
        sexo = input(f"Informe o sexo da pessoa {pessoa} [M/F]: ").strip().upper()
        if sexo in ['M', 'F']:
            break
        else:
            print("Sexo inválido! Informe 'M' para masculino ou 'F' para feminino.")

    soma_idade += idade

    if sexo == 'M':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome

    elif sexo == 'F' and idade < 20:
        mulheres_menores_20 += 1

media_idade = soma_idade / 4

print(f"\nMédia de idade do grupo: {media_idade:.2f}")
if nome_homem_mais_velho:
    print(f"Homem mais velho: {nome_homem_mais_velho} com {idade_homem_mais_velho} anos")
else:
    print("Não há homens no grupo.")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menores_20}")


