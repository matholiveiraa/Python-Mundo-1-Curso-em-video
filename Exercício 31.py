#Um programa que pergunte a distância de uma viagem em km
#Calcule o preço da passagem por r$0.50 por km para viagens até 200km
#Acima disso r$0.45

import time
print("Iremos fazer um programa que calculará o valor de uma viagem por cada km rodado")
time.sleep(2)
km = int(input("Digite quantos km você quer viajar: "))

if km <= 200:
    km = km*0.50
    print(f"{km} esse é valor que você deve pagar")
else:
    km > 200
    km = km*0.45
    print(f"\33[1;32m{km} esse é o seu valor para pagar da viagem!")