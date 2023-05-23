# Métodos de classe
# São métodos onde "self" será "cls", Ou seja
# ao invés de receber a instãncia no primeiro parametro
# receberemosa própria classe

class Pessoa:
  ano = 2023 # atributo de classe
  
  def __init__(self,nome,idade):
    self.nome = nome
    self.idade = idade
  
  @classmethod
  def metodo_de_classe(cls):
    print('Hey')
    
  @classmethod
  def criar_com_50_anos(cls,nome):
    return cls(nome,50)
  
  @classmethod
  def criar_sem_nome(cls,idade):
    return cls('Anonima',idade)
    
Pessoa.metodo_de_classe()

p1 = Pessoa('João',34)
p2 = Pessoa.criar_com_50_anos('Davi')
print(vars(p2 ))
p3 = Pessoa.criar_sem_nome(23)
print(vars(p3))