"""
args - Argumentos não nomeados
-> *args (enpacotamento e desenpacotamento)
"""

# Lembre-te de desenpacotamento
x,y, *resto = 1,2,3,4
print(x, y, resto)


def soma(x,y):
  return x + y

def soma2(*args):
  total = 0
  for numero in args:
     total += numero
  return total

print(soma2(1,2,3,4,5,7))
print(sum((1,2,3,4,5,7)))