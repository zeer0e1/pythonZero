"""
Introducao ao desempacotamento + tuples (tuplas)
"""
lista = ['Lucas','Sky']
#nome1,nome2 = lista

# Pegando someente o primeiro valor
nome1, *r =  ['Lucas','Sky']

#Jeito correto de se fazer o desempacotamento
nome1, *_ =  ['Lucas','Sky']

# Pegando somente o nome 2

_,nome2 = ['Lucas', 'Sky']