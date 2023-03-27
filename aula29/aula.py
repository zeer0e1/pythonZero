"""
Introducao ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero = input("Vou dobar o numero que vc digitar: ")


try:
    numero_float = float(numero)
    print(f'O dobro de {numero} é {numero_float * 2:.2f}')
except:
    print('Isso não é número')
