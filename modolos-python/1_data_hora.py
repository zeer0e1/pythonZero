# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

# from pytz import timezone

data = datetime.now()
print(data.timestamp())
# data_str_data = '2022-04-20 15:01:1'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'
# # data = datetime(2023, 4, 20, 15, 1)
# data = datetime.strptime(data_str_data, data_str_fmt)
# print(data)
# data_atual = datetime.now(timezone('Asia/Tokyo'))

# print(data_atual)

print(datetime.fromtimestamp(1686077970))
