import time

saldo_da_conta = 2500.39
quantidade_de_saques = 0
dia_ultimo_saque = time.localtime().tm_mday 
movimentacoes_saque = []
movimentacoes_deposito = []

while True:
  dia_atual = time.localtime().tm_mday

  if dia_atual != dia_ultimo_saque:
    quantidade_de_saques = 0
    dia_ultimo_saque = dia_atual

  print("""
  1 - Extrato
  2 - Saque
  3 - Deposito
  4 - Sair
  """)


  opcao = int(input("Selecione a opção desejada: \n"))
  print()


  match(opcao):
    case(1):
      if movimentacoes_saque == [] and movimentacoes_deposito == []:
        print('Não foram realizadas movimentações na conta')
        print("O seu saldo atual é: R$ {:.2f}".format(saldo_da_conta))
        print()
      else:
        print('Depósitos \t')
        for movimentacao in movimentacoes_deposito:
          print(movimentacao, sep='\n')
        print('Saques')
        for movimentacao in movimentacoes_saque:
          print(movimentacao, sep='\n')
        print()
        print("O seu saldo atual é: R$ {:.2f}".format(saldo_da_conta))
        print()

    case(2):

      print('Valor máximo de saque: R$ 500,00')
      print('Quantidade máxima de saques por dia: 3')
      print(f'Saques realizados hoje: {quantidade_de_saques}')
      print()
    
      while True:
        if quantidade_de_saques == 3:
          print('Você já atingiu o máximo de saques no dia de hoje')
          break

        print("Digite o valor do saque ou digite 0 para cancelar a operação")
        valor_saque = float(input("R$ "))
        print()
        if valor_saque > 500:
          print("Valor máximo de saque é de R$ 500,00!")
          print()

        elif valor_saque > saldo_da_conta:
          print("Saldo insuficente")

        elif valor_saque == 0:
          print("Saque cancelado")
          break

        else:
          saldo_da_conta -= valor_saque
          print("Saque realizado com sucesso")
          print("Agora o seu saldo é de: R$ {:.2f}".format(saldo_da_conta))
          print()
          movimentacoes_saque.append(f'- R$ {valor_saque:.2f} ({time.localtime().tm_mday:02d}/{time.localtime().tm_mon:02d} as {time.localtime().tm_hour:02d}:{time.localtime().tm_min:02d})')
          quantidade_de_saques +=1
          break

    case(3):
      print("Digite o valor para depósito ou digite 0 para cancelar a operação. \t")
      valor_deposito = float(input("R$ "))
      print()

      if valor_deposito > 0:
        saldo_da_conta += valor_deposito
        print()
        print(f"Agora o seu saldo é de R$ {saldo_da_conta:.2f}")
        print()
        movimentacoes_deposito.append(f'+ R$ {valor_deposito:.2f} ({time.localtime().tm_mday:02d}/{time.localtime().tm_mon:02d} as {time.localtime().tm_hour:02d}:{time.localtime().tm_min:02d})')
      else:
        print("Depósito cancelado")
        print()

    case(4):
      break
    case _:
      print("Opção inválida")
      print()
