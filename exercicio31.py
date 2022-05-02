distancia = int(input('Digite a distância da viagem'))
if distancia <= 200:
    print('Você percorreu {} e o preço é R${}'.format(distancia,distancia * 0.50))
else:
    print('Você percorreu {} e o preço é R${}'.format(distancia,distancia * 0.45))