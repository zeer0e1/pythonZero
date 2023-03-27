# interpolacao básica de string
# s - string
# d e i = int
# f - float
# x e X - hexadeciamal
nome = 'Lucas'
preco = 1000.454545
variavel = '%s, o preco é R$%.2f' % (nome,preco)
print(variavel)
print('O hexadecimal de %d é %x'% (15,15))