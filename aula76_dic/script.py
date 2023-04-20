# Dicionários em Python ( tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor"
# Chaves podem ser consideredas com indice
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# o valor pode ser de qualquer tipo, incluindo outro dicionario
# usas as chaves {} ou classe dict para criar dicionários
# Imutáveis: str, int, float, bool, tuple
# mutável: dict, list
pessoa1 = {
       'nome': 'Lucas',
       'sobrenome': 'Freitas',
       'idade': 26,
       'altura': 1.78,
       'enderecos' : [
             {'rua': 'logo ali', 'numero': 123},
             {'rua': 'aqui perto', 'numero':456}
       ]
 }

print(pessoa1 , type(pessoa1))

for chave in pessoa1:
      print(chave, pessoa1[chave])

pessoa = {}

pessoa['nome'] = 'Lucas'

#Criando chave dinamica
chave = 'nome'
pessoa[chave] = 'Ribeiro Gonçalves'

pessoa['sobrenome'] = 'Lucas'

print(pessoa[chave])

pessoa[chave] = 'Freitas'

print(pessoa[chave])

print()
print(pessoa)


#Deletando um chave
del pessoa['sobrenome']

# Veriicando se a chave existe utilizando um meto da tupla

if pessoa.get('sobrenone') is None:
      print('Existe')
else:
      print('N existe')