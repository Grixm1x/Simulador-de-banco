from datetime import datetime


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar(self, tipo, valor):
        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.transacoes.append(f"{tipo}: R$ {valor:.2f} em {data}")

    def exibir(self):
        return "\n".join(self.transacoes) if self.transacoes else "Nenhuma transação realizada."


class Conta:
    def __init__(self, agencia, numero, limite=500, limite_saques=3):
        self.agencia = agencia
        self.numero = numero
        self.saldo = 0
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0
        self.historico = Historico()

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar("Depósito", valor)
            return True
        return False

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        if valor > self.limite:
            print("Valor excede o limite de saque.")
            return False
        if self.saques_realizados >= self.limite_saques:
            print("Número de saques excedido.")
            return False
        self.saldo -= valor
        self.saques_realizados += 1
        self.historico.adicionar("Saque", valor)
        return True

    def exibir_extrato(self):
        print("==== Extrato ====")
        print(self.historico.exibir())
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("=================")


class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.conta = Conta(agencia="0001", numero="12345")


nome = input("Nome do cliente: ")
cpf = input("CPF: ")
data_nascimento = input("Data de nascimento: ")
endereco = input("Endereço: ")

cliente = Cliente(nome, cpf, data_nascimento, endereco)

while True:
    print("\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "d":
        valor = float(input("Valor do depósito: "))
        if cliente.conta.depositar(valor):
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Valor do saque: "))
        cliente.conta.sacar(valor)

    elif opcao == "e":
        cliente.conta.exibir_extrato()

    elif opcao == "q":
        print("Obrigado por usar o sistema bancário!.")
        break

    else:
        print("Opção inválida, Tente novamente.")
