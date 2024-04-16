# Desafio do módulo "... Python e Suas Estruturas de Dados" do Bootcamp VIVO.


menu = """
    Escolha uma opção:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [cu] Cadastrar Usuário
    [cc] Cadastrar Conta
    [q] Sair
"""


saldo = 0
extrato = ""
limiteDiario = 3
numeroDeSaques = 0
valor = 0
usuarios = []
contas = []

def filtrar_usuarios(cpf, usuarios):
    if usuarios is not None:
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                return True
            else:
                return False

def saque(saldo=saldo, valor=valor, extrato=extrato, limiteDiario=limiteDiario, numeroDeSaques=numeroDeSaques):
    valorLimiteDeSaque = 500

    if valor > valorLimiteDeSaque:
        return "Você não pode sacar mais que o limite de R$500,00."
    elif numeroDeSaques >= limiteDiario:
        return "Você já atingiu o limite diário de saques para o dia de hoje."
    elif valor > saldo:
        return f"Saldo insuficiente para essa transação.\n Saldo: {saldo}."
    else:
        saldo -= valor
        numeroDeSaques += 1
        extrato += f"- Saque de R${valor:.2f}.\n"
        print(f"Valor de {valor} sacado com sucesso!")
    return saldo, extrato, numeroDeSaques

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"+ Deposito de R${valor:.2f}.\n"
        print(f"Valor de {valor} depositado com sucesso!")
    else:
        print("Coloque um valor maior que 0!")
    return saldo, extrato

def get_extrato(saldo, /, *, extrato=extrato):
    if extrato:
        return f"{extrato} \n Saldo: {saldo:.2f}."
    else:
        return f"Nenhuma movimentação realizada."

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números):")

    if filtrar_usuarios(cpf, usuarios):
        print("Já existe usuário com este CPF cadastro. Utilize outro CPF ou faça o login.")
        return
    
    nome = input("Informe o nome completo:")
    nascimento = input("Informe a data de nascimento:")
    endereco = input("Informe o endereço:")
    usuarios.append({"nome":nome, "data_nascimento":nascimento, "cpf":cpf, "endereco":endereco})
    print("Usuário cadastrado com sucesso!")
    filtrar_usuarios(cpf, usuarios)

    return usuarios

def cadastrar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário para o qual deseja criar uma conta:")
    numero_conta = len(contas) + 1
    usuario_exists = filtrar_usuarios(cpf, usuarios)

    if usuario_exists:
        print("Conta criada com sucesso!")
        return {"agencia":"0001", "conta":numero_conta, "usuario":cpf}
    else:
        print("Não existe usuário cadastrado com este CPF! Crie primeiro o usuário.")
        return

while True:
    opcao = input(menu)
    match opcao:
        case "d":
            valor = float(input("informe o valor que deseja depositar:"))
            saldo, extrato = (deposito(saldo, valor, extrato))
            
        case "s":
            valor = float(input("Informe o valor que deseja sacar:"))
            saldo, extrato, numeroDeSaques = saque(saldo=saldo, valor=valor, extrato=extrato, limiteDiario=limiteDiario, numeroDeSaques=numeroDeSaques)
            
        case "e":
            print(get_extrato(saldo, extrato=extrato))
            
        case "cu":
            usuarios = cadastrar_usuario(usuarios)

        case "cc":
            conta = cadastrar_conta(contas, usuarios)
            if conta:
                contas.append(conta)

        case "q":
            break
        case _:
            opcao = input("escolha uma opção válida!")
        