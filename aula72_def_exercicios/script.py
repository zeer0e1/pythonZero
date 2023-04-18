# Exercicios com funções
# Crie uma função que multiplique todos os argumentos
# não nomeados recebidos
# Retorne o total par auma variável e mostre o valor 
# da variavel

def multi_numeros(*numeros):
  total = 0
  for numero in numeros:
    total += numero * numero
  return total

print(multi_numeros(2,2))