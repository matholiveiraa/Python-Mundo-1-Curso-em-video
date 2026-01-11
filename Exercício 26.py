#Um programa que lerá a frase e mostrará
#Quantas vezes aparece a letra letra A
#Em que posição a primeira vez
#Em que posição ela aparece pela ultima vez

frase=input("Digite a frase: ").lower().strip()

print(frase.count("a")) #contar quantos a tem

print(frase.find("a")+1) #ver onde começa o a

print(frase.rfind("a")) #posição em que aparece pela ultima vez

