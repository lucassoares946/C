conta_normal = False
conta_universitaria = False

saldo = 2000

cheque_especial = 450

saque = int(input("Digite o valor a ser sacado 💵"))

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso 💵")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado utilizando cheque especial 💳")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente 🥲")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso 💵")
    else:
        print("Saldo Insuficiente 🥲")

else:
    print("Sistema fora do Ar 👨‍💻")


