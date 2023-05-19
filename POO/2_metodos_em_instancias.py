# Métodos em instãncias de classes python
#Hard coded - É algo escrito diretamente no código
class Carro:
    def __init__(self,nome,cor,qtd_portas):
        self.nome = nome
        self.cor = cor
        self.qtd_portas = qtd_portas

    def acelerar(self):
        print(f'{self.nome} acelerou .....')

fusca = Carro('Fusca','Branco',2)
print(fusca.nome,fusca.cor,fusca.qtd_portas)
fusca.acelerar()