#Faça um programa que nem o anterior mas agora terá um dos 4 ser o primeiro
#E de assim em diante quem fará a proxima apresentação 
#Um programa que dê random em um do nome dos quatro alunos
import random
import time
print("Iremos sortear um dos quatro alunos, quem irá apresentar primeiro!")
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
for C in range (4):
    alunoremovido1 = random.choice(listaalunos)
    print(f"Siga as colocações: {alunoremovido1}")
    time.sleep(2)
    listaalunos.remove(alunoremovido1)