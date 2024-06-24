menu = """
[1] Depositar 
[2] Sacar
[3] Consultar Extrato
[0] Sair 

"""

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("Depósito")
        valor = float(input("Digite o valor que deseja depositar em R$: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(extrato)    
        else:
          print("Valor digitado inválido")

    elif opcao == 2:
        numero_saques = 0
        print("Saque")
        valor = float(input("Digite o valor que deseja sacar em R$: "))

        if valor > saldo:
            print("Não foi possível realizar a operação, porque você não possui saldo suficiente!")

        elif valor > limite:
            print("Não foi possível realizar a operação, porque o valor excede o limite de saque permitido!")

        elif numero_saques >= LIMITE_SAQUES:
            print("Não foi possível realizar a operação, porque o número de saques foi excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques +=1
        else:
            print("Valor digitado inválido")

    elif opcao == 3:
        print("Consulta Extrato")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção digitada inválida") 