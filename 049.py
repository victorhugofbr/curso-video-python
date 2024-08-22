"""
EXERCÍCIO 049: Tabuada v2.0

Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.
"""

n = int(input("Informe um número para exibir sua tabuada: "))
print("*"*30)
for i in range(0,11):
    print(f"{n} x {i} = {n*i}")
print("*"*30)
