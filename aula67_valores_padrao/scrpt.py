"""
Valores padrão para parametros
Ao definir uma função, os parametros podem
ter valores padrão. Caso o valor não seja
enviado para o parametro, o valor padrão será 
usado
"""

def soma(x,y,z=0):
  if z is not None:
    print(x + y + z)
  else:
    print(f'{x=} {y=}', x + y)


soma(1,2)
soma(100,200)