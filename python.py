print(f"""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
      )
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    enter = input("Escolha a operação desejada ")

    if enter == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Digite um deposito valido")

    elif enter == "s":
        valor = float(input("Informe o valor do saque: "))
        if numero_saques < LIMITE_SAQUES:
            if valor <= limite:
                if saldo >= valor:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f"Saque: R$ {valor:.2f}\n"

                else:
                    print("Não foi possivel realizar o saque, saldo insuficiente")

            else:
                print("Você nãõ possui saldo o suficiente")
        else:
            print("Limite de saques exedidos")
    elif enter == "e":
        print("===============Seus exratos===============")
        print(extrato if extrato else "Não ocorreu nenhum extrato")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif enter == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
