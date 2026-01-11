#Escreva um programa que leia a velocidade de um carro

#Caso ultrapassar de 80km/h aparece dizendo msg q foi multado

#Multa custa 7.00r$ por cada km/h acima do limite

import time

print("Veremos quantos km/h o sujeito passou acima do limite")
time.sleep(2)
print("A cada 1km/h acima do limite acrescenta r$7.00")

velocidade = int(input("Digite a velocidade: "))

conta = velocidade - 80


if velocidade > 80:
    print(f"O sujeito deverá pagar: {conta * 7}")
else:
    print("\33[1;34mA velocidade estava OK, muito obrigado!")