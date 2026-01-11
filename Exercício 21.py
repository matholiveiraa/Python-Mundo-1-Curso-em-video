#Faça um programa que abra um aúdio de um aquivo em mp3

#Um programa que dê random em um do nome dos quatro alunos
import random
import time
import playsound
print("Iremos sortear um dos quatro alunos para apagar o quadro!")
time.sleep(2)

a1 = str(input("Digite o nome do primeiro aluno: "))
time.sleep(1)
a2 = str(input("Digite o nome do segundo aluno: "))
time.sleep(1)
a3 = str(input("Digite o nome do terceiro aluno: "))
time.sleep(1)
a4 = str(input("Digite o nome do quarto aluno: "))

listaalunos = [a1,a2,a3,a4]

time.sleep(2)
contador = 0
for C in range (3):
    contador += 1
    print(f"O sorteado aparecerá em {contador}...")
    time.sleep (1)

print(f"O sorteador foi: {random.choice(listaalunos)}")
playsound.playsound('conffeti.mp3') 