import random

for _ in range(10):

  cpf = ''

  for i in range(9):
    cpf += str(random.randint(0,9))

  cpf_limpo = list(cpf.replace('.','').replace('-',''))
  cpf_nove_digitos = cpf_limpo[:9]
  contador_regressivo1 = 10
  contador_regressivo2 = 11
  soma_digito1 = 0
  soma_digito2 = 0




  for index, numero in enumerate( cpf_limpo):
    if index < 9:
      soma_digito1 += contador_regressivo1 * int(numero)
      contador_regressivo1 -= 1

  calculo_digito1 = (soma_digito1 * 10) % 11

  calculo_digito1 = calculo_digito1 if calculo_digito1 <= 9 else 0


  cpf_limpo.append(calculo_digito1)
  for index,numero in enumerate(cpf_limpo):
    if index < 10:
      soma_digito2 +=  contador_regressivo2 * int(numero)
      contador_regressivo2 -=1
    calculo_digito2 =(soma_digito2 * 10) % 11

  calculo_digito2 = calculo_digito2 if calculo_digito2 <= 9 else 0

  cpf_nove_digitos.append(calculo_digito1)
  cpf_nove_digitos.append(calculo_digito2)

  novo_cpf = ''.join(str(n) for n in cpf_nove_digitos)
  print(novo_cpf)