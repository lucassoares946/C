sal = int(input('Digite o seu salario'))
if sal > 1250:
    print('Seu salario agora é {}'.format((sal * 0.10)+ sal))

if sal <= 1250:
        print('Seu salario agora é {}'.format((sal * 0.15) + sal))