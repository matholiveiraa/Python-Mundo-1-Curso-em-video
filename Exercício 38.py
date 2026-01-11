#Leia o comprimento de três reta e me diga se pode ser um triangulo ou não
#A < B + C (A é menor que a soma de B e C).
#B < A + C (B é menor que a soma de A e C).
#C < A + B (C é menor que a soma de A e B).

import time

print("Veremos se é possível formar um triângulo com os dados que você irá digitar")
time.sleep(2)

print("Começa agora!")
time.sleep(2)
lado1 = int(input("Digite o primeiro lado: "))
time.sleep(1)
lado2 = int(input("Digite o segundo lado: "))
time.sleep(1)
lado3 = int(input("Digite o terceiro lado: "))

teste = 0

if lado1 < lado2 + lado3:
    teste += 1
if lado2 < lado1 + lado3:
    teste += 1
if lado3 < lado1 + lado2:
    teste += 1

if teste == 3:
    print("\33[1;32mPode ser um triângulo!")
else:
    teste < 3
    print("\33[1;31mNão pode ser um triângulo")