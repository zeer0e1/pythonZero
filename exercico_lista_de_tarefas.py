import os
def limpar_tela():
     os.system('cls')

todo = []
lixeira =[]
comandos = ['Listar','Desfazer', 'Refazer']


limpar_tela()

def adicionar_tarefa (tarefa,list):
    list.append(tarefa)

def mostrar_tarefas (list):
    for i in list:
        print(i)

def remover_tarefa(list):
    ultima_taefa  = list.pop()
    lixeira.append(ultima_taefa)
    mostrar_tarefas(list)


while True:
   
    print('Comandos: ', end=' ')
    for comando in comandos:
        print(comando,end=' ',sep=',')
    print('')
    escolha = input('Digite uma tarefa ou comando: ')

    if  escolha in comandos:
        if escolha == 'Listar':
            mostrar_tarefas(todo)
        elif escolha == 'Desfazer':
             remover_tarefa(todo)
        elif escolha == 'Refazer':
            print(lixeira[len(lixeira) - 1])
            adicionar_tarefa(lixeira[len(lixeira) - 1],todo)
        elif escolha == 'Sair':
            break  
       
    else:
        adicionar_tarefa(escolha,todo)


