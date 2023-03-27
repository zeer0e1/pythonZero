"""
constante  variaveis que não tem o valor alterado
Muitas condicções no mesmo if = ruim

"""

velocidade = 61
local_carro = 90

RADAR_1 = 60
LOCAL_1 =100
RADAR_RANGE = 1



if local_carro >= (LOCAL_1 + RADAR_RANGE) and local_carro \
    <= (LOCAL_1 + RADAR_RANGE) and vel_carro_pass_radar_1:
    print("Carro multado em rada 1")