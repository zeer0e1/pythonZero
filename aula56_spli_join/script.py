"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = 'Olha só que, coisa interessante'

# Usando assim ele vai criar uma nova lista dividindo
# a string por espaços em branco
lista_palavras = frase.split()
print(lista_palavras)

# utilizando um delimitador de até onde vai cada pedaço
lista_palavras2 = frase.split(',')
print(lista_palavras2)

#Retirando os espaços dos ites da lista
# for i, frase in enumerate(lista_palavras2):
#   lista_palavras2[i] = lista_palavras2[i].strip()

print(lista_palavras2)

# O recomendado é melhor criar uma lista nova para salvar essa novas infos
lista_nova = [] 

#Retirando os espaços dos ites da lista e colocando esses itens em uma nova lista
for i, frase in enumerate(lista_palavras2):
  lista_nova.append(lista_palavras2[i].strip())
print(lista_nova)


# Unindo lista/string com join
frases_unidas = '-'.join('abc')
print(frases_unidas)

#Unindo lista com join
frases_unidas2 = ''.join(lista_nova)
print(frases_unidas2)