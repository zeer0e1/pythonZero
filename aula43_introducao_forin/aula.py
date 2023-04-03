texto = 'Python'

i = 0

tamanho_string = len(texto)
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)
