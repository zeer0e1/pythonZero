class Pessoa:
    ANO_ATUAL = 2023

    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ANO_ATUAL - self.idade


p1 = Pessoa('Lucas',26)
p2 = Pessoa('Rau',21)

#print(p1.__dict__) # guarda os dados da instancia do meu objeto
print(vars(p1)) # mostra os atributos da minha instancia
print(p1.get_ano_nascimento())
p1.nome = 'Zé'
print(vars(p1))
print(p2.get_ano_nascimento())