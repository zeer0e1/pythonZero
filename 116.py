import os

caminho_arquivo = 'C:\\Users\\lucasg\\Documents\\zero\\pythonZero\\'
caminho_arquivo += 'aula116.txt'


# with open (caminho_arquivo,'w+') as arquivo:
#     arquivo.write('Linha 1 \n')
#     arquivo.write('Linha 2 \n')
#     arquivo.writelines(
#         ('Linha 3 \n', 'Linha 4 \n')
#     )
#     arquivo.seek(0,0)
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0,0)
#     print(arquivo.readline(),end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print('READLINES')
#     arquivo.seek(0,0)
#     for linha in arquivo.readlines(): 
#         print(linha.strip())

# print('#' * 4)

with open (caminho_arquivo,'w+', encoding='utf-8') as arquivo:
    arquivo.write('Atenção \n')
    arquivo.write('Linha 1 \n')
    arquivo.write('Linha 2 \n')
    arquivo.writelines(
        ('Linha 3 \n', 'Linha 4 \n')
    )
  

os.remove(caminho_arquivo)

