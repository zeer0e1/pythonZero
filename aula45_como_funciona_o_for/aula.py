"""
Iterável -> str, range, etc
Interador -> quem sabe entregar um valor por vez
next -> me entrege o próximo valor
iter -> me entregue seu iterador
"""

numeros = range(0, 100, 2)

texto = 'Luiz'
iterador = iter(texto)
for numero in numeros:
    print(numero)

# Isso e o que for faz

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break