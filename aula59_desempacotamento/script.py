# Desempacotamento em chamadas
# de métodos e funções

string = 'abc'
lista = ['A' , 'Q','X','l','G']
tupla = 'Lucas','Freitas','Ribeiro'

a,b,c = tupla
p,b, *_,e = lista
print(a,b)
print(e)
print(*lista, sep='\n')