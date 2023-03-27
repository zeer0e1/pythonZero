hora_atual = input('Digite o horário atual: ')

try:
    hora_float = float(hora_atual)
    if hora_float >= 0 and hora_float <= 11:
        print('Bom dia')
    elif hora_float >= 12 and hora_float <= 17:
        print('Boa tarde')
    elif hora_float > 17 and hora_float <= 23:
        print('Boa noite')
except:
    print('Erro')