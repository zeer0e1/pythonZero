import os 
os.system('cls')
print('Escolha uma das opções: ')
lista_compras = []
while True:
  escolha = input('[i]nserir [a]pagar [l]istar [s]air : ')
  if escolha == 'i':
    print('Digite o item que você quer adicionar na lista: (digite "t" para voltar ao menu)')
    while True:
      item = input()
      if item == 't':
        break
      else:
        lista_compras.append(item)
        continue 
    
  elif escolha == 'l':
    for i, item in enumerate(lista_compras, start=1):
        print(i, item)
    continue
  elif escolha == 'a':
    for i, item in enumerate(lista_compras, start=1):
        print(i, item)
    print()
    index = input('Digite o número do item que vc deseja excluir: ')
    try:
      lista_compras.pop(int(index) - 1)
    except:
      os.system('cls')
      print('Numero fora da lista tente novamente.')
      index = input('Digite o número do item que vc deseja excluir: ')
      lista_compras.pop(int(index) - 1)
    finally:
      print('Item excluido')
  elif escolha == 's':
    break
    
