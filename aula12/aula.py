nome = 'Lucas'
altura = 1.68
peso = 78.4
imc = peso / altura ** 2
print(imc)

# f-strings
linha_1 = f'{nome} tem {imc:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'

print(linha_1)
print(linha_2)
