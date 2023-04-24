"""
Métodos uteis dos dicionarios em Python
len - qantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se uma chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com chave específica ( del)
popitem - apga o último item
update - atualiza um dicionário com outro
"""
import copy
pessoa1 = {
       'nome': 'Lucas',
       'sobrenome': 'Freitas'
 }

# Mostra a quantidade de chaves do dicionarios
print(len(pessoa1))

# Mostra as chaves do dict
print(pessoa1.keys())

# Mostra os valores
print(f' aaaaaaaaaa {pessoa1["sobrenome"].values()}')

# Mostra a chave e o valor
print(pessoa1.items())

# Usado para definir um valor padrão para uma chave
pessoa1.setdefault('idade', 10)
pessoa1.setdefault('nome','anonimo')
print(pessoa1['nome'])

# Shallow copy
d1 = {
      'c1' : 1,
      'c2' : 32      
}

# Usando o sinal de igual a o dicionario d2 vai apontar para o mesmo
# Local da variavel d1 e se eu alterar um o outro tbm é alterado
d2 = d1

d2['c1'] = 1000

# Para copiar somente os valores utilizamos o método copy()
# Esse método copia somente os valores imutaveis do dicionarios
# O que for mutável é linkado e vai apontar para o mesmo lugar da variavel copiada
d2 = d1.copy()

# Para copiar todos os valores é necessário importar o módulo copy
# E depois utilizar o deepcopy() que seria a copia profunda

d2 = copy.deepcopy(d1)

# Get retorna  uma chave

p1 ={
      'nome': 'Lucas',
      'sobrenome' : 'Ribeiro',
      'ultima_chave': 'fon'
}

print(p1.get('nome'))

# Pop apaga um item específico mas esse valor pode ser salvo
# Se atribuirmos esse valor a uma variável

nome = p1.pop('nome')
print(nome)
print(p1)

# popitem - apaga o último item adicionado

ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)

# update atualiza um dicionário com outro
print('-' * 10)
p1.update({
      'nome': 'novo valor',
      'idade': 30
})
tupla = (('chav1','valor chave1'), ('chav2','valor chave2'))
lista = [['chave3', 'valor chave 3'],['chave4','valor chave4']]
print(p1)
p1.update(tupla)
print(p1)
p1.update(lista)
print(p1)

