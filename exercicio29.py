
velocidade = int(input('Digite a velocidade do carro'))
if velocidade > 80:
    print('Você sera multado em R${}'.format((velocidade - 80) * 7))
else:
    print('Nada de multa')