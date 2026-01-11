#Um programa que faça o computador pensar um numero
#o usuario deve acertar esse numero
#e contabilizar os erros

import time
import playsound
import random
from random import randint

print("Vamos fazer um brincadeira!")
time.sleep(2)
print("Você vai ter de acertar um numero entre 0 e 5")
time.sleep(2)


sorteio = randint(0,5) #Fiz um sorteio de um número inteiro na variavel sorteio de 0 a 5


n = int(input("Digite seu número: "))

if n != sorteio:
    print("Você errou")
else:
    n == sorteio
    print("Você ganhou!")
    playsound.playsound("conffeti.mp3")
