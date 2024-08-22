# Faça um programa que mostre na tela
# Uma contagem regressiva para o estouro e fogos de artifício,
# Indo de 10 até 0, com uma pausa de 1 segundo entre eles.
# USANDO LOOP AGORA

import time

for elm in range(10,-1,-1):
    print(f"{elm}")
    time.sleep(1)

print("BOOM KABUM BOOM KABUM BOOM!!!!!")
print("Feliz ano novo!")