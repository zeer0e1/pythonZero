class Animal:
    def __init__(self,nome):
        self.nome = nome
    def acao(self):
        return f'{self.nome} está executando acão'
    
leao = Animal('Leão')
