menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("------ DEPOSITO ------")
        valor = float(input("Digite valor do deposito?"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operação inválida!")

    elif opcao == "2": 
        print("------ SAQUE ------")
        valor = float(input("Digite valor do saque:"))
        
        saldo_insuficiente = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("Saldo Insuficiente!")

        elif excedeu_limite:
            print("Valor saque excedeu limite!")

        elif excedeu_saque:
            print("Número de saques diario excedido!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Valor informado é inválido!")

    elif opcao == "3":
        print("\n------ EXTRATO ------")
        print("Não foram realizadas movimentações!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-----------------------")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
