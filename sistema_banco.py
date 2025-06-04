# CRIAR UM SISTEMA BANCÁRIO COM EXTRATO, SAQUE, E DEPÓSITO. PRECISA SER POSSIVEL REALIZAR 3 DEPOSITOS COM LIMITE DE R$500, CASO O USUARIO NÃO TENHA SALDO PRECISA EXIBIR UMA MENSAGEM QUE O USUARIO NÃO TEM SALDO DISPONIVEL. NO FINAL DA OPERAÇÃO PRECISA SER LISTAD TODOS OS DEPOSITOS E SAQUES 

menu = """

=========== Bem-Vindo =============

Qual operação deseja realizar ?

[1] Saque
[2] Deposito
[3] Extrato
[4] Sair

====================================

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
       print(f"Seu saldo é de R${saldo:.2f}")
       saque = float(input("Quanto deseja sacar R$: "))

       excedeu_saldo = saque > saldo

       excedeu_limite = saque > limite

       excedeu_saques = numero_saque >= LIMITE_SAQUES

       if excedeu_saldo:
           print("Operação Falhou, Saldo Insuficiente")

       elif excedeu_limite:
           print("Operação Falhou, Valor de saque excedeu o limite")

       elif excedeu_saques:
           print("Você esgotou seu número de saques")

       elif saque > 0:
           saldo -= saque
           extrato += f"Seu saque foi de R$: {saque:.2f}\n2"
           numero_saque += 1   
       
       else:
        print("Operação Falhou! O valor informado é inválido")              


    elif opcao == "2":
        print(f"Seu saldo é de R$: {saldo:.2f}")
        deposito = float(input("Quanto deseja depositar R$:"))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito Realizado R$: {deposito:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido")    


    elif opcao == "3":
        print("\n=================EXTRATO===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSeu saldo é de R$: {saldo:.2f}")
        print("=============================================")

    elif opcao == "4":
        break        

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada")  