# List comprehension em python
# É uma forma simples e rápida para criar as listas
# a partir de interáveis

# Maneira de outras linguagens utilizar 
lista1 = []

for numero in range(10):
  lista1.append(numero)

# Maneira python de fazer isso 
lista2 = [numero * 2 for numero in range(10)]

print(lista2)