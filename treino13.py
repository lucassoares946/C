import math
ca1 = float(input('Digite o valor do primeirto cateto '))
ca2 = float(input('Digite o valor do segundo cateto '))
hyp = math.hypot(ca1,ca2)
print('Valor da hipotenusa {:.2f}'.format(hyp))