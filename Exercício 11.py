#Calcule a largura e altura de uma parede em metros
#calcule aa area e quantidade de tinta necessário para pinta-lá
#Cada litro de tinta pinta uma área de 2m²

largura = int(input("Digite a largura da parede: "))
altura = int(input("Digite a altura da parede: "))
areaparede = largura * altura
tinta = 2

print(f"área da parede: {areaparede}, seria necessário, metros de tinta: {areaparede/tinta}")