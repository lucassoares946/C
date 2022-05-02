from random import randint
computador = randint(0,5)
jogador = int(input('Digite um numero entre 0 e 5'))
if jogador == computador:
    print('Você ganhou digitou {} e eu {}'.format(computador,jogador))
else:
    print('Você perdeu eu pensei no numero {} e voce digitou {}'.format(computador,jogador))
