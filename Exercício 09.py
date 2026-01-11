#Faça um número que leia um número e faça sua tabuada até o 10

import time

print("Faremos um programa para você que calculará a tabuada até 10!")

time.sleep(2)

n = int(input("Digite o valor que quer a tabuada: "))

contador = 0

for C in range(n,n*10+1,n):
    contador += 1
    print(f"{n} x {contador} = {C}")