# Exercicio - sistema de perguntas e respostas
perguntas = [
  {
    'Pergunta': 'Quanto é 2+2',
    'Opções': ['1','3','4','5'],
    'Resposta': '4'
  },
   {
    'Pergunta': 'Quanto é 5 * 5',
    'Opções': ['25','55','10','51'],
    'Resposta': '25'
  },
   {
    'Pergunta': 'Quanto é 10/2',
    'Opções': ['4','5','2','1'],
    'Resposta': '5'
  }
]


def imprimir_opcoes(opcoes):
  for ind ,opcao in enumerate(opcoes):
    print(f'{ind}) {opcao}')

def valida_resposta(dic):
  opcao_ecolhida = input()
  resposta_correta = dic['Resposta']
  if opcao_ecolhida == resposta_correta:
    print('Você acertou !!')
  else:
    print('Você errou...')


def imprimir_pergunta(dic):
  print(f'Pegunta: {dic["Pergunta"]}')
  imprimir_opcoes(dic["Opções"])
  valida_resposta(dic)
  
for i, pergunta in enumerate(perguntas):
  imprimir_pergunta(pergunta)

