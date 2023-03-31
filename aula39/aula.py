"""
Iterando strings com while
"""

nome = 'Lucas Freitas'
tamanho_nome = len(nome)
contador = 0
nova_string = ''
nome_inverso = ''

while contador < tamanho_nome:
    nova_string += f'*{nome[contador]}'
    contador += 1

print(nova_string)
print(nome_inverso)
