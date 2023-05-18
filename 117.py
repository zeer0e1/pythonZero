import json

# pessoa = {
#     'nome': 'Lucas',
#     'sobrenome': 'Fretas',
#     'enderecos' : [
#         {'Rua': 'R1', 'numero' :32},
#         {'Rua': 'R2', 'numero' :31},
#     ],
#     'altura' : 1.6,
#     'numeros_preferidos': (2,4,6,8,10),
#     'dev': True,
#     'nada' : None,
#     }

# with open('aula117.json','w') as arquivo:
#     json.dump(pessoa,
#               arquivo,
#               indent=2 
#               )

with open('aula117.json','r',encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(pessoa['nome'])