#Crie um programa que leia o nome de uma cidade
#Diga se ela começa ou não com o nome santo

import time

print("Você nos dará o nome de uma cidade e nós iremos dizer se ela começa com santo ou não!")

cidade = input("Digite o nome da cidade: ")
cidade = cidade.lower()
divisao = cidade.split()


print("santo" in divisao[0])