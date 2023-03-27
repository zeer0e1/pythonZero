numero = input('Digite um número inteiro: ')
try:
    numero_float = float(numero)
    if numero_float % 2 == 0:
        print('é par')
    else:
        print('é impar')
except:
    print('Vc digitou um número inválido')