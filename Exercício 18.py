#Faça um programa que leia um ângulo qualquer
#Ele deve mostrar na tela o valor de
#seno
#tangente
#cosseno

import time
import math

print("Iremos fazer um programa para você que calcula o SENO, COSSENO, TANGENTE de um ângulo...")

time.sleep(2)

print("Vamos lá?")

time.sleep(2)

n1 = float(input("Digite o valor que você deseja está permitido número também não inteiros: "))
n1 = math.radians(n1)

print(f"Seno do ângulo é: {math.sin(n1)}")
time.sleep(1)
print(f"Cosseno do ângulo é: {math.cos(n1)}")
time.sleep(1)
print(f"Tangente do ângulo é: {math.tan(n1)}")
time.sleep(1)
print("Obrigado por testar!")