import os

lista = {'TI01': 'pedrod', 'TI02': 'Williamp', 'NTB-LUCASG': 'lucasg', 'NTB-PAULOM':'PAULOM'}
servidor = ''
continuar = True


def menu_escolha():
    print('ESCOLHE UMA DAS OPÇÕES AE BOBO: ')
    for indice, (chave, valor) in enumerate(lista.items()):
        print(' ', indice + 1, valor.upper())


def usuarios():
    while True:
        escolha = int(input())
        match escolha:
            case 1:
                servidor = 'TI01 pedrod'
                return servidor
            case 2:
                servidor = 'TI02 WILLIAMP'
                return servidor
            case 3:
                servidor = 'NTB-LUCASG lucasg'
                return servidor
            case 4:
                servidor = 'NTB-PAULOM PAULOM'
                return servidor
            case _:
                print('Opção incorreta, tente novamente')
                continue


def enviar_mensagem(mensagem):
    os.system(f'MSG /server:{servidor} {mensagem}')


menu_escolha()

servidor = usuarios()


while continuar:
    msg = input('DIGITA ALGO AE (0 = SAIR  1 = TROCAR USUARIO): ')
    if msg == '0':
        continuar = False
    elif msg == '1':
        menu_escolha()
        servidor = usuarios()
    else:
        if msg == '':
            continue
        enviar_mensagem(msg)
        os.system('cls')
