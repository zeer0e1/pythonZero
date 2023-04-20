# Exercicios com funções
# Crie uma função que multiplique todos os argumentos
# não nomeados recebidos
# Retorne o total par auma variável e mostre o valor 
# da variavel

def multi_numeros(*numeros):
  total = 1
  for numero in numeros:
    total *= numero
  return total
   

multi = multi_numeros(2,3,4,5,6)
print(multi)

# Crie uma função que fala se o número é par ou impar
# retorne se o número é par ou impar

def chek_number(number):
  if number % 2 == 0:
    print(f'The number {number} is even')
  else:
    print(f'The number {number} is uneven')

chek_number(3)