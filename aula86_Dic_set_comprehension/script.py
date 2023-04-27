# Dictionary comprehension e Set comprehension
import pprint

def p (v):
  pprint.pprint(v,compact= True,width=40)

produto = {
  'nome': 'Caneza azul',
  'preco': 2.5,
  'categoria': 'Escritório'
}
dc = {
  chave:  valor if isinstance(valor, (int, float)) else valor.upper() for chave, valor in produto.items()
  if chave == 'categoria'
}

p(dc)

