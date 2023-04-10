"""
Enumrate - enumera iteráveis (indices)
"""
lista = ['Lucas','Freitas','Gonçalves']
lista.append('Joao')

for i,item in enumerate(lista, start=2):
  print(i,item)