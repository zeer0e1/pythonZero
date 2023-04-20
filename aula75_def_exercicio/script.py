# Exercicio
# crie funções que duplicam, triplicam e quadruplicam
# o número recebido como paramentro

def duplicar_numero(number):
  return number * 2

def triplicar_numero(number):
  return number * 3

def quadruplicar_numero(number):
  return number * 4

def operacao(number,func1,func2,func3):
  return func1(number), func2(number), func3(number)

result = operacao(2,duplicar_numero,triplicar_numero,quadruplicar_numero)

print(result)


# Solucao do professor
def criar_multiplicador(multi):
  def multiplicar(number):
    return number * multi
  return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))