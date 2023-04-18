"""
Introducao as funções (def) em Python
Funções são trechos de código usados para replicar
determinada ação ao longo do seu código 
e retornar um valor específico
por padrão, funções Python retornam
"""
def imprimir(a='vazio' ,b='Vazio2', c='Vazio3'):
  print(f'{a,b,c}')

imprimir('Lucas','Freitas','Ribeiro')

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
    
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)