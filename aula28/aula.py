nome = input('Digite seu nome: ')
idade = input('Digite sua idade ')
if nome and idade:
    print(f'Seu nome é {nome} \n'
          f'Seu nome invertido é {nome[::-1]} \n'
          f'Seu nome contém (ou não) espaços {" " in nome} \n'
          f'Seu nome contém {len(nome)} letras \n'
          f'A primeira letra do seu nome é {nome[0]} \n'
          f'A última letra do seu nome é {nome[len(nome) -1]}')
else:
    print("Desculpe, você deixou campos vazios")
