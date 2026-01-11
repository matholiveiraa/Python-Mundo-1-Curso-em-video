#Crie o programa que leia o nome completo de uma pessoa
#E mostre:
#O nome com todas as letras maisculas
#O nome com todas as letras minusculas
#Quantas letras ao todo(sem considerar espaços)
#Quantas letras tem no primeiro nome

import time
print("Você terá que digitar o nome completo...")
time.sleep(2)
nome = str(input("Digite seu nome: "))

print(nome.upper())
print(nome.lower())

nomesem = nome.strip()
print(len(nome))
 
nome1 = nome.split()
print(len(nome1[0]))