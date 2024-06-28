from datetime import datetime

menu = """
---------- MENU ----------

      SEJA BEM VINDO!
  Escolha uma das opções

        [1] DEPOSITAR
        [2] SACAR
        [3] EXTRATO
        [4] SAIR
  
--------------------------
"""

saldo = 0.0
limite_dinheiro = 500.0
extrato = []
numero_saque = 0
LIMITE_SAQUE = 3

#Inicio do programa
while True:

    #inicio menu
    print(menu)
    try:
        #Escolher opção (Caso o valor digitado for uma letra ou simbolo ira retornar para essa opção).
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Valor digitado é inválido. Tente novamente")
        continue
    
    #Inicío opção depositar
    if opcao == 1:
        while True:
            #Escolher o valor de depósito (Caso o valor digitado for uma letra ou simbolo ira retornar para essa opção).
            try:
                valor_deposito = float(input("Valor a depositar: R$ "))
            except ValueError:
                valor_deposito = None #limpa a variavel para evitar depositar o mesmo valor
                print("\nValor digitado é invalido.\nTente novamente ou digite 0 (ZERO) para ir ao MENU.")
                continue

            if valor_deposito is None: #limpa a variavel para evitar que seja depositado o mesmo valor em caso de erro
                continue

            if valor_deposito > 0:
                saldo += valor_deposito
                data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                extrato.append(f"{data_hora} - Depósito: R$ {valor_deposito:.2f}")
                print(f"\nDepósito de R$ {valor_deposito:.2f} realizado com sucesso.\n")
                break
            elif valor_deposito == 0:
                break
            else:
                print("\nERRO! Tente novamente ou digite 0 (ZERO) para sair.\n")
    #Fim depositar

    #Inicio saque
    elif opcao == 2:
        while True:
            #Escolher o valor de saque (Caso o valor digitado for uma letra ou simbolo ira retornar para essa opção).
            try:
                valor_saque = float(input("Valor de saque: R$ "))
            except ValueError:
                valor_saque = None #comando para limpar valor na variável
                print("Valor digitado é invalido.\nTente novamente ou digite 0 (ZERO) para ir ao MENU.")
                continue
            if valor_saque is None: #comando para limpar valor da variável
                continue

            if valor_saque <= limite_dinheiro and (valor_saque > 0):
                if valor_saque <= saldo and LIMITE_SAQUE > 0:
                    LIMITE_SAQUE -= 1
                    saldo -= valor_saque
                    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    extrato.append(f"{data_hora} - Saque: R$ {valor_saque:.2f}")
                    print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.\nVocê ainda pode fazer {LIMITE_SAQUE} saques.")
                    break
                elif valor_saque <= saldo and LIMITE_SAQUE == 0:
                    print("Seu limite de saque está excedido!\nVerifique seu limite de saque no extrato.")
                    break
                elif valor_saque > saldo:
                    print("Saldo insuficiente para esse saque. Verifique seu extrato.")
                    break
                else:
                    print("ERRO. TENTE NOVAMENTE.\nOU DIGITE 0 (ZERO) PARA IR AO MENU.")
            elif valor_saque == 0:
                break        
            else:
                print(f"Seu limite de saque é de R$ {limite_dinheiro:.2f}.\nTente novamente ou digite 0 (ZERO) para ir ao n")            
    #Fim saque
     
    #Inicio extrato            
    elif opcao == 3:
        print("\n--------- EXTRATO ----------\n")
        if extrato:
            for transacao in extrato:
                print(transacao)
        else:
            print("Não foram realizadas transações.")
        print(f"\nSALDO: R$ {saldo:.2f}")
        print(f"LIMITE DE SAQUE RESTANTE: {LIMITE_SAQUE}")
        print(f"LIMITE PARA SAQUE POR VEZ: R$ {limite_dinheiro:.2f}\n")
    #Fim extrato

    #Inicio sair
    elif opcao == 4:
        print("\nObrigado por usar nosso sistema.\nVolte sempre!")
        break
    #Fim sair

    else:
        print("Erro. Escolha uma opção novamente.\n")
#Fim do programa