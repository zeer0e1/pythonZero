def zipper(lista1, lista2):
    intervalo_maximo = min(len(l1), len(l2))
    return [
        (l1[i], l2[i]) for i in range(intervalo_maximo)
    ]


l1 = ['Salvador', 'ubatuba', 'Belo horizonte']
l2 = ['Ba', 'SP', 'MG', 'RJ']

# funcao builtin do python

print(list(zip(l1, l2)))

# funcao para utilizar a lista maior

from itertools import  zip_longest

print(list(zip_longest(l1, l2, fillvalue='Sem cidade')))
