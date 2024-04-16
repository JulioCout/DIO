# Desafio 1 do módulo "POO" do Bootcamp VIVO.

menu = """
    Escolha uma opção:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [cu] Cadastrar Usuário
    [cc] Cadastrar Conta
    [q] Sair
"""

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    def saldo(self):
        pass

    def nova_conta(self):
        pass

    def sacar(self, valor):
        valorLimiteDeSaque = 500

        if valor > valorLimiteDeSaque:
            return "Você não pode sacar mais que o limite de R$500,00."
        elif valor > saldo:
            return f"Saldo insuficiente para realizar esse saque."
        else:
            saldo -= valor
            print(f"Valor de {valor} sacado com sucesso!")
        return True
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Valor de {valor} depositado com sucesso!")
        else:
            print("Coloque um valor maior que 0!")
            return False
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self.limite = 3
        self.limite_saque = 500

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transação(self, transacao):
        self.transacoes.append(transacao)

class Transacao:
    def __init__(self, conta):
        self.conta = conta
    
    def registrar(self, conta):
        return conta
    
class Saque(Transacao):
    def __init__(self, conta, valor):
        super().__init__(conta)
        self.valor = valor

class Deposito(Transacao):
    def __init__(self, conta, valor):
        super().__init__(conta)
        self.valor = valor




# while True:
#     opcao = input(menu)
#     match opcao:
#         case "d":
#             valor = float(input("informe o valor que deseja depositar:"))
#             saldo, extrato = (deposito(saldo, valor, extrato))
            
#         case "s":
#             valor = float(input("Informe o valor que deseja sacar:"))
#             saldo, extrato, numeroDeSaques = saque(saldo=saldo, valor=valor, extrato=extrato, limiteDiario=limiteDiario, numeroDeSaques=numeroDeSaques)
            
#         case "e":
#             print(get_extrato(saldo, extrato=extrato))
            
#         case "cu":
#             usuarios = cadastrar_usuario(usuarios)

#         case "cc":
#             conta = cadastrar_conta(contas, usuarios)
#             if conta:
#                 contas.append(conta)

#         case "q":
#             break
#         case _:
#             opcao = input("escolha uma opção válida!")
        