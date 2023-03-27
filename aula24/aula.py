# operadores in e not in
# Strings são iteraveis
nome = 'Lucas'
print(nome[2])

print('as' in nome)
print('z' not in nome)

sobrenome = input('Digite seu nome : ')
encontrar = input('Dgite o que vc quer encontrar: ')
if encontrar in sobrenome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')