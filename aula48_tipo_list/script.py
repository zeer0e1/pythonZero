"""
Lista em python
Tipo List - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis -> indices e fatiamentos
métodos uteis: append, insert, pop, del, clear, extend, +++
"""

string = 'ABCDE'
lista = ['Texto', 123, True, 1.2, []]
print(lista)
lista[0] = 'Lucas'
print(lista)

# adicionar no final da lista
lista.append('Olá')

# Remover do final da lista
lista.pop()

# inserindo em uma posição especifica na lista
# Recebe como argumento o indiece e o valor que vai ser colocado nesse indice
lista.insert(0, 5)

# Como juntar as listas
lista_a = [1, 2, 3, 4]
lista_b = [4, 6, 7, 8]
lista_c = lista_a + lista_b
print(lista_c)

# coloca a lista de dentro do extend dentro da lista anterior
lista_d = lista_a.extend(lista_b)
print(lista_a)

"""
Cuidado com dados mutáveis

= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memória (mutável)
"""

nome = 'Lucas'
noutra_variavel = nome
nome = 'Freitas'
print(nome)
print(noutra_variavel)
