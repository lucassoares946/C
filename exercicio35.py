a = float(input('Digite o primeiro valor'))
b = float(input('Sigite o segundo valor'))
c = float(input('Digite o terceiro valor'))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar triangulo')
else:
    print('Os segmentos acima não podem formar triangulo')
