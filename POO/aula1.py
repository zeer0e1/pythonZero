# Class - classes são moldes para criar novos objetos
# As classes geram novos objetos ( instancias) que podem
# ter seus próprios atributos e métodos.
# Os objetos grrados pela calsse podem usar seus dados 
# internos para realizar várias ações
# por convecnção, usamos PascalCase para nomes de classe

# string = 'Lucas' # str
# print(string.upper())
# print(isinstance(string,str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome



p1 = Pessoa('Lucas','Ribeiro')
# p1.nome = 'Lucas'
# p1.sobrenone = 'Freitas'

p2 = Pessoa('Rauana','Camargo')
# p1.nome = 'Rau'
# p1.sobrenone = 'Camargo'

print(p1.nome)
print(p2.nome)