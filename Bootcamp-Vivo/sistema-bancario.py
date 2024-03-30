
menu = """
    Escolha uma opção:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""


saldo = 0
extrato = ""

def saque(valor):
    global saldo
    global extrato
    if valor <= saldo: 
        saldo -= valor
        print(f"Valor de {valor} sacado com sucesso!")
        extrato += f"- Saque de R${valor:.2f}.\n"
    else:
        print("Saldo insuficiente para esse saque!")


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
            f"\n Saldo: {saldo:.2f}.\n"
        case "q":
            break
        case _:
            opcao = input("escolha uma opção válida!")
        