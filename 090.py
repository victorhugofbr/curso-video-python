
dados = {}

nome = input("Informe seu nome: ")
media = float(input("Informe sua Média: "))


dados['Nome'] = nome
dados['Média']= media

if dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'

elif dados['Média'] <7 and dados['Média'] >= 5:
    dados['Situação'] = 'Recuperação'

else:
    dados['Situação'] = 'Reprovado'


print("-"*30)
for k,v in dados.items():
    print(f"{k} é igual a {v}")




