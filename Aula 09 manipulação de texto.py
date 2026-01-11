#Vamos testar fatiamento aqui
#Nessa aula, vamos aprender operações com String no Python. 
#As principais operações que vamos aprender são o Fatiamento de String, 
#Análise com len(), count(), find(), transformações com replace(), 
#upper(), lower(), capitalize(), title(), strip(), junção com join().


#Lembrando que parte brancas que nem o espaço do teclado tbm contam na frase
frase = "Curso em vídeo Python"
print(frase[9]) #aqui estamos testando o 9 elemento dentro da string
print(frase[9:14]) #vamos do V até O de vídeo
print(frase[9:21:2]) #Aqui vamos escrever mas ele vai saltando de 2 em 2
print(frase[:5]) #começar do início até o 5
print(frase[15:]) #Indica o início mas não sabe o final!
print(frase[9::3]) #Vai começar no nove e vai até o final pulando de 3 em tres
print(len(frase)) #O len serve para mostrar o total de espaços da frase
print(frase.count('o')) #Ele irá contar quantas vezes a letras O aparece!
print(frase.count('o',0,14))#contar quantos O tem do início até o 13 elemento que vai até vídeo
print(frase.find("o")) #começa apartir do 4 elemento
print(frase.find("Android")) #Me retorna o valor -1 significada falso
print("Curso" in frase)#Valor True o false se exister curso na frase
print(frase.replace("Python","JavaScript")) #Apenas substitui no print e não muda a variavel
print(frase.upper())#Me dará a frase em total maiuscula
print(frase.lower())#Me dará a frase em total minuscula
print(frase.capitalize()) #Pega a inteira inteira e deixa apenas o primeiro caractere dela para maiscula
print(frase.title())#Ele deixa todas as palavras com a primeira caractere maiscula

frase1 = "   Aprenda Python  "
print(frase1.strip()) #Serve para remover espaços excedentes na frase
print(frase1.rstrip()) #Remove somente os ultimos espaços
print(frase1.lstrip()) #Remove somente os primeiros espaços
print(frase.split())# Ele vai fazer a divisão dos espaços e cada palavra ficara fora da outra, ou seja ele gera uma lista
print("-".join(frase))#Junta todas as palavras com um tracinho no espaço entre cada