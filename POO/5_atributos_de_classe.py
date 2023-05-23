class Pessoa:
    ANO_ATUAL = 2023

    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ANO_ATUAL - self.idade


p1 = Pessoa('Lucas',26)
p2 = Pessoa('Rau',21)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())