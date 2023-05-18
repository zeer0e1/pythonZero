def adiciona_clietens(nome, lista=[]):
    lista.append(nome)
    return lista


cliente1 = adiciona_clietens('Luiz')
adiciona_clietens('Lucas', cliente1)
print(cliente1)