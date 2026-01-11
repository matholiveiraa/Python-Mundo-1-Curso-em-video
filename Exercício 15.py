#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
#e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmrodado = 0.15
dia = 60

n = int(input("Digite o valor de km rododas com o carro: "))
n1 = int(input("Digite quantos dias você ficou com o carro: "))

n3 = n1 * dia
calculokmrodado = n * kmrodado

print(f"O valor de dias ficou em: R${n3} e o valor de km rodado ficou: R${calculokmrodado}")
print(f"O total ficaria: \033[1;32mR${n3 + calculokmrodado}")
