# Para criar uma funcao lambda o python recomenda que seja criada uma função que execute as funções lambda 

# Essa é a função que vai executar as nossas funções lambda
def executa(funcao, *args):
  return funcao(*args)

# Como transformar essa função em uma função lambda
def soma (x,y):
  return x + y

def cria_multiplicador(multiplicador):
  def multiplica(numero):
    return numero * multiplicador
  return multiplica

# Uma função normal
print(soma(1,2))

# Tranformando em lambda
print(executa(
  lambda x, y: x + y # Isso seria a funcao
        ,2,3 # Esse seria os parametros da funcao
))

# Então temos a função executa 
# que recebe 2 argumentos
# 1 Uma função
# 2 os argumentos 
# e retorna a função passada por argumento com o
# argumentos passando como parametro para essa funcao
