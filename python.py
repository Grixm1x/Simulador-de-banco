import pytz
import datetime
d = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
data_Fmt = d.strftime("%d/%m/%y %Hh:%M")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
numero_depositos = 0
LIMITE_SAQUES = 3
LIMITE_DEPOSITOS = 10
nome = input("nome usuario ")
idade = input("idade usuario ")
usuaio = {"nome": {nome}, "idade": {idade}, }
print(f"""s

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

{data_Fmt}
=> """
)
while True:

    enter = input(f"Escolha a operação desejada {nome} ")

    if enter == "d":
        if numero_depositos < LIMITE_DEPOSITOS:
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                numero_depositos += 1
                extrato += f"Depósito: R$ {valor:.2f}, Horario: {data_Fmt}\n"

            else:
                print("Digite um deposito valido")
        else:
            print("Limite de deposito atingido")

    elif enter == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Informe o valor do saque: "))
            if valor <= limite:
                if saldo >= valor:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f"Saque: R$ {valor:.2f}, Horario: {data_Fmt}\n"

                else:
                    print("Não foi possivel realizar o saque, saldo insuficiente")

            else:
                print("Você nãõ possui saldo o suficiente")
        else:
            print("Limite de saques atingido")
    elif enter == "e":
        print("===============Seus exratos===============")
        print(f"""Informações do usuario: 
              Nome:{nome}, Idade: {idade}""")
        print(extrato if extrato else "Não ocorreu nenhum extrato")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif enter == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
