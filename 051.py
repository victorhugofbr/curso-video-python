"""
EXERCÍCIO 051: Progressão Aritmética

Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""


primeiro_termo = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão da progressão aritimética: "))


decimo_termo = primeiro_termo + (10 - 1) * razao

print("*"*30)
print("Progressão aritimética")
print("*"*30)

for elm in range(primeiro_termo,decimo_termo + razao,razao):
    print(elm,end=' ')
