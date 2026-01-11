#Aula de módulos e importaçõoes tais como math 
import random #serve para gerar numeros aleatórios
import math
import emoji 
from math import sqrt #Essa daqui é a raiz quadrada por exemplo

n1 = float(input("Digite o número que deseja saber a raiz quadrada: "))

listadeteste = [10,20,30,40,50,60,70,80,90,100]

print(f"A raiz quadrada de {n1} é: {math.sqrt(n1):.2f}") #primeiro eu jogo a biblioteca, depois a função que desejo e dentre parenteses jogo a variavel
#:.2f duas casas decimais depois de ponto

print(f"O número sorteado de listadeteste é: {random.choice(listadeteste)}")

