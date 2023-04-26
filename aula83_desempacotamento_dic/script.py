# Empacotamento e desempacotamento de dicionários

a,b = 1,2

pessoa = {
  'nome': "Aline",
  "sobrenome": 'Souza'
}

a,b = pessoa.values()
print(a,b)

#
(a1,a2), (b1,b2) = pessoa.items()
print(a1,a2,b1,b2)

#desempacotando um dicionario

dados_pessoa = {
  'idade': 26,
  'sobrenome':'Freitas'
}
                   # utilizando 2 * para jogar o conteudo do dicionario dentro desse novo dicionario
pessoa_completa = {**pessoa, **dados_pessoa}

def mostro_argumentos_nomeado(*args, **kwargs):
  print(kwargs)

mostro_argumentos_nomeado(nome="Lucas",teste=123)