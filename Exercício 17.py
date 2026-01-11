#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
#calcule e mostre o comprimento da hipotenusa

import time
import math

print("Iremos calcular a hipotenusa para você: ")
time.sleep(2)
catetooposto = float(input("Digite o valor do cateto oposto: "))
time.sleep(2)
catetoadjacente = float(input("Digite o valor do cateto adjacente: "))
time.sleep(2)
conta = math.pow(catetoadjacente,2) + math.pow(catetooposto,2) #pow de elevado, ,2 de elevado a 2
hipotenusa = math.sqrt(conta)
print(f"O valor da hipotenusa seria: {hipotenusa:.2f}")

