# os   + shutil - copiando arquvios com python
# 1 vamos copiar arquvios de uma pasta para outra
# mover / Renomear -> shutil.move
# Mover / Renomear -> os.rename
# Copiar -> shutil.copy
# Apagar -> os.unlink
# Apagar diretórios recursivamente -> shutil.rmtree
import os
import shutil
from itertools import count

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Script SQL')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA')

# os.makedirs(NOVA_PASTA, exist_ok=True)

shutil.rmtree(NOVA_PASTA)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminho_novo_diretorio = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)
#         os.makedirs(caminho_novo_diretorio, exist_ok=True)

#     for file in files:
#         caminho_original = os.path.join(root, file)
#         caminho_novo_arquivo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
#         )
#         shutil.copy(caminho_original, caminho_novo_arquivo)

#         print(file)
lista = {'TI01': 'pedrod', 'TI02': 'Williamp', 'NTB-LUCASG': 'lucasg', 'NTB-PAULOM':'PAULOM'}

print('ESCOLHE UMA DAS OPÇÕES AE BOBO:  se quiser fechar tecle 0')
for indice, (chave, valor) in enumerate(lista.items()):
    print(' ', indice + 1, valor.upper())
escolha = int(input())

match escolha:
    case 1:
        servidor = 'TI01 pedrod'
    case 2:
        servidor = 'TI02 WILLIAMP'
    case 3:
        servidor = 'NTB-LUCASG lucasg'
    case 4:
        servidor = 'NTB-PAULOM PAULOM'
    case _:
        print('Nava haver escolhe outro')
print('Agora é digitar a mensagem seu bobo')
msg = input()
os.system(f'MSG /{servidor} msg')
# servidor = input('Digite o nome do pc e o nome do usuário: ')
# msg = input('Digite a mensagem: ')
# os.system(f'MSG /server:{servidor} {msg}')
