"""
Repetições 
Executa uma ação enquanto uma condição for verdadeira
‘Loop’ infinito é quando um codigo não tem fim
"""
contador = 0

while contador <= 10:
    contador += 1

    if contador == 6:
        continue

    print(contador)

print('Acabou')
