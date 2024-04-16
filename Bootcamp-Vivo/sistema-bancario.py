# Desafio do módulo "Python Essencial e..." do Bootcamp VIVO

menu = """
    Escolha uma opção:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""


saldo = 0
extrato = ""
limiteDiario = 3

def saque(valor):
    global saldo
    global extrato
    global limiteDiario
    valorLimiteDeSaque = 500

    if valor > valorLimiteDeSaque:
        print("Você não pode sacar mais que o limite de R$500,00.")
    elif limiteDiario == 0:
        print("Você não pode sacar mais do que 3 veses no dia.")
    elif valor > saldo:
        print("Saldo insuficiente para essa transação.")
        print(f"Saldo: {saldo}") 
    else:
        saldo -= valor
        limiteDiario -= 1
        print(f"Valor de {valor} sacado com sucesso!")
        extrato += f"- Saque de R${valor:.2f}.\n"


def deposito(valor):
    global saldo
    global extrato
    if valor > 0:
        saldo += valor
        print(f"Valor de {valor} depositado com sucesso!")
        extrato += f"+ Deposito de R${valor:.2f}.\n"
    else:
        print("Coloque um valor maior que 0!")


while True:
    opcao = input(menu)
    match opcao:
        case "d":
            valor = float(input("informe o valor que deseja depositar:"))
            deposito(valor)
            
        case "s":
            valor = float(input("Informe o valor que deseja sacar:"))
            saque(valor)
            
        case "e":
            print("Nenhuma movimentação realizada." if not extrato else extrato)
            print(f"\n Saldo: {saldo:.2f}.\n")
        case "q":
            break
        case _:
            opcao = input("escolha uma opção válida!")
        