"""
Calculadora com while
"""
print('Como é o seu nome ? ')
nome = input()
print(f'Seja bem vindo(a), {nome}')
operacao = input('Qual o tipo de operação você quer realizar ? ( + - / *): ')
while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    try:
        numero1_convertido = float(numero1)
        numero2_convertido = float(numero2)

        if operacao == '+':
            print(f'O resultado da operação é {numero1_convertido} {operacao} {numero2_convertido} ={numero1_convertido + numero2_convertido}')
        elif operacao == '-':
            print(f'O resultado da operação é {numero1_convertido} {operacao} {numero2_convertido} ={numero1_convertido - numero2_convertido}')
        elif operacao == '*':
            print(f'O resultado da operação é {numero1_convertido} {operacao} {numero2_convertido} ={numero1_convertido * numero2_convertido}')

        opecao = input('\nDeseja:\n[s]air\n[c]ontinuar\n[t]rocar de operacao : ').lower()

        if opecao == 's':
            print('Programa encerrado...')
            break
        elif opecao == 'c':
            continue
        elif opecao == 't':
            operacao = input('Qual o tipo de operação você quer realizar ? ( + - / *: ')
        else:
            print('Operacao inválida')
            continue
    except:
        print('Você não digitou um número')
