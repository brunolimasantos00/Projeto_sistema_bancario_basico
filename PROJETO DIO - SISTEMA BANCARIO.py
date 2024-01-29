saldo = 0
limite = 500
extrato = " "
numero_saque = 0
limite_saque = 3

menu = '''
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR

'''
while True:
    opcao = input(menu)
    
    if opcao == "1":
        print("DEPOSITO")
        valor = float(input("informe o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor: .2f} \n'
        else:
            print("Falha na operação. Valor informado nao é válido. Por favor tente novamente!!!")
    
    elif opcao == "2":
        valor = float(input("Informe o valor do SAQUE:"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_num_saque = numero_saque >= limite_saque
        
        if excedeu_saldo :
            print("OPERAÇÃO NAO CONCLUIDA - SALDO INSUFICIENTE!!!")
            
        elif excedeu_limite :
            print("OPERAÇÃO NAO CONCLUIDA: VALOR DO SAQUE ULTRAPASSA O LIMITE DIARIO!!!") 
            
        elif excedeu_num_saque :
            print("OPERAÇÃO NAO CONCLUIDA: NUMERO DE SAQUE EXCEDIDO!!!")
            
        elif valor > 0:
            saldo -= valor
            extrato += f'saque: R$ {valor: .2f}\n'
            numero_saque += 1
        else :
            print("OPERAÇÃO NAO CONCLUIDA: VALOR INFORMADO É INVALIDO!!!!")
    
        
    elif opcao == "3":
        print("********** EXTRATO **********")
        print("NÃO HÁ MOVIMENTAÇAO." if not extrato else extrato)
        print(f'\nSALDO R$ {saldo: .2f}')
        print("******************************")
      
        
    elif opcao == "4":
        print("SAIR !!! Obrigado por utilizar nossos serviços!")
        break
        
    else:
        print("INFORME UMA OPÇÃO VÁLIDA")
