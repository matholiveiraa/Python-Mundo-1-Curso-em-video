#Faça um programa de aumento salarial
#if maior que 1250 aumento de 10%
#se nao se menor ou igual 1250 aumento de 15%

import time

print("O patrãoa agora quer aumentar salário de todos!!")
time.sleep(2)
print("Aumento de 10% para maior que 1250")
print("Aumento de 15% para iguais a ou menor que 1250")

time.sleep(3)

salario = int(input("Digite o salário: "))

if salario > 1250:
    print(f"Com reajuste ficaria {salario + (salario*0.10)}")
else:
    salario <= 1250
    print(f"O novo reajuste ficaria: {salario + (salario*0.15)}")