# isinstance - para sabber se o objeto é de determinado tipo

lista = ['a',1,1.1,True, [0,1,2], (1,2), {0,1},{'nome': 'Luiz'}]


for item in lista:
  if isinstance(item,str):
    print(item.upper(), isinstance(item,set))

  if isinstance(item,(int,float)):
    print(item)
    print('é numeral')