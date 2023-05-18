import json
import os

to_do_list = []
recycle_todo = []
commands = ['Listar','Desfazer','Refazer','Sair']
file_name = 'todolist.json'
list_save = []


def verify_todolist_exist():
  if os.path.isfile(file_name):
        print('arquivo existe')
        with open(file_name,'r',encoding='utf8') as arquivo:
            list_save = list(json.load(arquivo))
            to_do_list.extend(list_save)
            


def view_list ():
    print('\n' * 2)
    print('TAREFAS')
    for todo in to_do_list:
        print(todo)

def add_todo (todo):
    to_do_list.append(todo)
    view_list()

def undo_task():
    if to_do_list:
      exclude_todo = to_do_list.pop()
      recycle_todo.append(exclude_todo)
      view_list()
    else:
        print('Não existe mais nada para Desfazer.')

def redo_task():
    if recycle_todo:
      last_todo_exclude = recycle_todo.pop()
      to_do_list.append(last_todo_exclude)
      view_list()
    else:
        print('Não tem mais nada na Refazer.')

def save_todo_list():
    list_save.extend(to_do_list)
    with open('todolist.json','w+') as arquivo:
        json.dump(list_save,arquivo)
        
verify_todolist_exist()

while True:
    print('Comandos: Listar,Desfazer,Refazer,Sair')
    choice = input('Digite o que deseja: ')
    if choice in commands:
        if choice == 'Listar':
            view_list()
            continue
        elif choice == 'Desfazer':
            undo_task()
            continue
        elif choice == 'Refazer':
            redo_task()
            continue
        elif choice == 'Sair':
            save_todo_list()
            break
    else:
        add_todo(choice)
    
