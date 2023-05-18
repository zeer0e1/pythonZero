to_do_list = []
recycle_todo = []
commands = ['Listar','Desfazer','Refazer','Sair']

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
            break
    else:
        add_todo(choice)
    