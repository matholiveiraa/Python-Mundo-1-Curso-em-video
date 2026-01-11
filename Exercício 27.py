#Um programa que leia o nome completo
#Mostre o primeiro nome da pessoa e o ultimo nome dela separamente

nome = input("Digite seu nome completo: ").lower()

nome1 = nome.split()

print(nome1)

print(f"primeiro nome: {nome1[0]}")

print(f"ultimo nome: {nome1[-1]}")