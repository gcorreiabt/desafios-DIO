# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip().upper())
cupom = input().strip().upper()

if cupom == 'DESCONTO10':
  preco = preco - (descontos['DESCONTO10'] * preco)
  print(f'{preco:.2f}')

elif cupom == 'DESCONTO20':
  preco = preco - (descontos['DESCONTO20'] * preco)
  print(f'{preco:.2f}')
  
else:
  print(f'{preco:.2f}')