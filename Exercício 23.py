#Faça um programa que leia de 0 a 9999
#mostre na tela cada um dos dígitos separados

#Exemplo digite um número:1834

import time

print('''Faremos um programa para você que lhe mostrará as unidades, as dezenas, as centenas, e as milhar''')

n = input("Digite o valor: ")
unidade = n[3]
dezena = n[2]
centena = n[1]
milha = n[0]

print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milha}")


