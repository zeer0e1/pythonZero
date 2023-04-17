cpf = '746.824.890-70'
cpf_limpo = list(cpf.replace('.','').replace('-',''))
contador = 10
soma_itens = 0

for index, numero in enumerate( cpf_limpo):
  if index < 9:
    soma_itens += contador * int(numero)
    contador -= 1

calculo_digito = (soma_itens * 10) % 11

if calculo_digito > 9:
  print('O resultado é 0')
else:
  print(f'O resultado da conta é {calculo_digito}')