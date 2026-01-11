#Faça um programa que leia quanto de dinheiro uma pessoa tem na carteira e de o valor quanto ela consegue comprar de dolar!

import time

print("Faremos um programa que lerá quantos você pode comprar de dolar com o dinheiro que você possui!")

dinheiro = float(input("Digite o seu dinheiro: "))

dolar = 5.37

print(f"Você consegue comprar: \033[1;32m${dinheiro / dolar}")

