"""
EXERCÍCIO 037: Conversor de Bases Numéricas

Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:

- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal
"""
numero_inteiro = int(input('Informe um número inteiro qualquer: '))

print("Escolha a base de conversão:")
print("1 para Binário")
print("2 para Octal")
print("3 para Hexadecimal")

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'Número binário: {bin(numero_inteiro)[2:]}')
elif opcao == 2:
    print(f'Número octal: {oct(numero_inteiro)[2:]}')
elif opcao == 3:
    print(f'Número hexadecimal: {hex(numero_inteiro)[2:]}')
else:
    print('Opção inválida!')
