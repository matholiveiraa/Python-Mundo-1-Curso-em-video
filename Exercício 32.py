#Faça um programa e leia se ele é um ano bissexto

import time

print("Faremos um programa que ele lerá se um ano é bissexto!")

time.sleep(2)

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    print("É um ano bissexto!")
else:
    print("Não é um ano bissexto")
