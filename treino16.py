import random
a = str(input('Aluno:'))
b = str(input('Aluno:'))
c = str(input('Aluno:'))
d = str(input('Aluno:'))

lista = [a,b,c,d]

random.shuffle(lista)

print('A ordem sera ')
print(lista)

