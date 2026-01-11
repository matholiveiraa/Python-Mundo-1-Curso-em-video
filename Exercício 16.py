#Crie um programa que leia um número Real
#Qualquer pelo teclado e mostre na tela a sua porção inteira

#Ex: 12.378 quero só a parte do 12
import math
#math trunc serve para remover as casas decimais
n = float(input("Digite um número do conjunto dos Reais, sem ser inteiro: "))
nmath = math.trunc(n)

print(f"{int(n)}") #aqui seria usando o python cru
print(f"Usando a biblioteca math ficaria: {nmath}") #aqui seria usando a biblioteca já de math, mais intuitiva e rápida